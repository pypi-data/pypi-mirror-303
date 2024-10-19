"""
This module, app.py, serves as the primary entry point to the CDC Data Hub LAVA (CDH-LAVA) application. It initializes the application and sets up the endpoints for various services, including Alation.

The Alation service is specifically designed to manage and monitor Alation. It provides the following API endpoints:

    GET /alation/metadata_excel_file_download/{schema_id}: Retrieves an Excel metadata file from Alation based on the provided schema_id.
    POST /alation/metadata_excel_file_upload: Uploads an Excel metadata file to Alation via direct upload.
    GET /alation/metadata_json_file_download/{schema_id}: Retrieves a JSON metadata file from Alation based on the provided schema_id.
    POST /alation/metadata_json_file_upload: Uploads a JSON metadata file to Alation via direct upload.

The module also integrates other services of the CDH, which include CDC Tech Environment service, Azure Key Vault service, CDC Self Service, CDC Admin service, CDC Security service, and Posit service.

Besides, it includes HTTP enforcement, logging, exception handling, metrics reporting to Azure Monitor, and telemetry instrumentation functionalities.

The app is primarily designed to serve as an HTTP server for the CDH, exposing various functionalities as HTTP endpoints for file uploads, downloads, log access, and error presentation.

Usage:
python app.py

TODO:

There is a Flask-OAuthlib library that can be used to simplify the OAuth2 flow. It is not used in this project, but it might be worth considering for a future release.
"""

import cdh_lava_core.cdc_security_service.security_oauth as security_oauth
import cdh_lava_core.jira_service.jira_client as jira_client
import sys
import os
import time
import csv
import traceback
import subprocess
from datetime import datetime
import json
import base64
import ast
import requests
import jwt
from dotenv import load_dotenv
from jwcrypto import jwk
from urllib.parse import unquote
from functools import wraps
from werkzeug.datastructures import FileStorage
from requests.exceptions import RequestException
from flask import (
    redirect,
    send_file,
    request,
    render_template,
    Blueprint,
    jsonify,
    make_response,
    url_for,
    session
)
from flask_restx import Resource, fields, reqparse
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from flask_cors import CORS
import pandas as pd
from azure.monitor.opentelemetry.exporter import AzureMonitorMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry import metrics

try:
    from cdh_lava_core.app_startup import create_api, create_app
except ModuleNotFoundError as ex:
    trace_msg = traceback.format_exc()
    line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
    error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
    exc_info = sys.exc_info()
    # logger_singleton.error_with_exception(error_message, exc_info)
    raise ex


import cdh_lava_core.alation_service.db_schema as alation_schema
from cdh_lava_core.cdc_tech_environment_service import (
    environment_file as cdc_env_file,
)
from cdh_lava_core.az_key_vault_service import (
    az_key_vault as cdh_az_key_vault,
)
from cdh_lava_core.cdc_log_service.environment_logging import LoggerSingleton
from cdh_lava_core.cdc_log_service.environment_tracing import TracerSingleton
from cdh_lava_core.cdc_security_service import (
    security_core as cdh_security_core,
)
from cdh_lava_core.posit_service import (
    posit_connect as cdh_posit_connect,
)
from cdh_lava_core.altmetric_service.altmetric_downloader import AltmetricDownloader
from cdh_lava_core.excel_service.excel_config_uploader import ExcelConfigUploader
from cdh_lava_core.excel_service.excel_sheet_combiner import ExcelSheetCombiner 
from cdh_lava_core.az_storage_service.az_storage_file import AzStorageFile
from cdh_lava_core.databricks_service.dbx_db_rest.jobs import JobsClient
from cdh_lava_core.databricks_service.dbx_db_rest import RestClient
from cdh_lava_core.az_log_analytics_service.az_kql import AzKql

# Define hardcoded credentials for local development
HARD_CODED_USER = "Test User"
HARD_CODED_USER_ID = "test@cdc.gov"
USE_HARDCODED_LOGIN = os.getenv("USE_HARDCODED_LOGIN", "false").lower() == "true"

DATA_PRODUCT_ID = "lava_core"
TIMEOUT_5_SEC = 5
TIMEOUT_ONE_MIN = 60
# Get the currently running file name
SERVICE_NAME = os.path.basename(__file__)
# Get the parent folder name of the running file
NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
ENVIRONMENT = "dev"
ALLOWED_ORIGINS = [
    "http://localhost:5000",
    "http://localhost:8001",
    "https://login.microsoftonline.com",
    "https://rconnect.edav.cdc.gov",
    "https://rstudio.edav.cdc.gov",
]



print(f"SERVICE_NAME:{SERVICE_NAME}")
print(f"NAMESPACE_NAME: {NAMESPACE_NAME}")
sys.path.append(os.getcwd())
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_dir)

app = create_app()
# handle posit flask gateway
if 'RS_SERVER_URL' in os.environ and os.environ['RS_SERVER_URL']:
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1, x_proto=1, x_host=1)


def generate_code_verifier():
    return base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')

# Generate code_verifier and code_challenge
code_verifier = generate_code_verifier()

# handle posit flask gateway
@app.before_request
def before_request():

    if USE_HARDCODED_LOGIN:
        # Use hardcoded credentials when running locally or in Posit Workbench
        session['user_id'] = HARD_CODED_USER_ID
        request.user = HARD_CODED_USER
        print(f"Using hardcoded user: {HARD_CODED_USER}")
        if 'user_id' in session:
            request.user = session['user_id']
        else:
            request.user = None
        logger.info("HARDCODED_ROUTE")
    else:
        if 'user_id' in session:
            request.user = session['user_id']
        else:
            request.user = None

        # logger.info('Headers: %s', request.headers)
        logger.info('Scheme: %s', request.scheme)

        if request.headers.get('X-RStudio-Proto') == 'https':
            request.environ['wsgi.url_scheme'] = 'https'
            session.modified = True  # Force secure cookie

auth_parser = reqparse.RequestParser()
auth_parser.add_argument("code", type=str, help="Code parameter", location="args")
auth_parser.add_argument("state", type=str, help="State parameter", location="args")

auth_form_parser = reqparse.RequestParser()
auth_form_parser.add_argument("code", type=str, help="Code parameter", location="form")
auth_form_parser.add_argument(
    "state", type=str, help="State parameter", location="form"
)

# Apply CORS
config = app.cdc_config
edc_cors_url_list = config["edc_cors_url_list"]
url_array = edc_cors_url_list.strip("'").split(",")
print(f"cors url list: {str(url_array)}")
CORS(
    app,
    origins=ALLOWED_ORIGINS,
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Credentials",
    ],
    resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}},
    supports_credentials=True,
)


# Define the blueprint
cdc_admin_bp = Blueprint("logs", __name__, url_prefix="/logs")

# Define the blueprint
cdc_files_bp = Blueprint("files", __name__, url_prefix="/files")

# Define the blueprint
cdc_modules_bp = Blueprint("modules", __name__, url_prefix="/modules")


cdc_files_protected_bp = Blueprint(
    "protected_files", __name__, url_prefix="/protected_files"
)

altmetric_bp = Blueprint("altmetric", __name__, url_prefix="/altmetric")


def list_config_environments(directory):
    """
    List the middle part of filenames that start with 'config.' and end with '.json'.
    Example: 'config.dev.json' -> 'dev'
    """
    middle_parts = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the filename starts with 'config.' and ends with '.json'
        if filename.startswith('config.') and filename.endswith('.json'):
            # Extract the middle part (the part between 'config.' and '.json')
            middle_part = filename[len('config.'):-len('.json')]
            middle_parts.append(middle_part)
    
    return middle_parts

def get_rstudio_user_id():
    # Check if running inside RStudio Connect
    if 'RS_SERVER_URL' in os.environ  or 'rstudio' in request.headers.get('Host', '').lower():
        logger.info("RS_SERVER_URL found")
        
        cookie_header = request.headers.get('Cookie')

        # Optionally, parse the Cookie header manually if needed
        if cookie_header:
            logger.info("Cookie header found")
            cookies = cookie_header.split('; ')
            for cookie in cookies:
                logger.info(f"Cookie header: {cookie}")
                if cookie.startswith('user-id='):
                    rstudio_user_id_part = f"{cookie.split('=')[1]}"
                    # Extract the user-id by splitting on '|'
                    rstudio_user_id = rstudio_user_id_part.split('|')[0]
                    logger.info(f"user-id found in Cookie header: {rstudio_user_id}")

        else:
            logger.warning("No Cookie header found")
            
        # Log all headers to see what is being passed
        logger.info(f"Request headers: {request.headers}")


        # Extract the user ID from the RStudio Connect headers
        rstudio_user_id = request.headers.get('X-RStudio-User')
        if rstudio_user_id:
            return rstudio_user_id
    else:
        logger.info("RS_SERVER_URL not found")
    return None

def extract_id_token(set_cookie_header):
    # Split the header by '; ' to get individual cookies
    if set_cookie_header is None:
        return None
    cookies = set_cookie_header.split("; ")

    for cookie in cookies:
        # Split each cookie string by '=' to get the name-value pair
        name, _, value = cookie.partition("=")

        # Check if the cookie name is 'Id_token'
        if name == "id_token":
            return value
    return None


def check_and_return_error(id_token):
    try:
        # Try to parse the token as JSON
        # Print id_token to check its type and content
        print(f"id_token type: {type(id_token)}, id_token content: {id_token}")

        # If id_token is already a dictionary, skip json.loads
        if isinstance(id_token, dict):
            token_data = id_token
        else:
            token_data = json.loads(id_token)

        # Check if the "error" attribute exists
        if "error" in token_data:
            # Print the value of the "error" attribute
            return token_data["error"]
        else:
            return ""

    except json.JSONDecodeError:
        # If there's an error in decoding, the token is not valid JSON
        return ""


def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes} minutes, {secs} seconds"


def combine_urls(base_url, relative_url):
    if base_url.endswith("/"):
        # Remove trailing slash if it exists
        base_url = base_url[:-1]
    # Combine the cleaned base URL with the relative URL
    redirect_url = base_url + relative_url
    return redirect_url


def jwk_to_pem(jwk_dict):
    """
    Converts a JSON Web Key (JWK) into Public Key in PEM format.

    The function uses the jwcrypto library to convert a JWK from dictionary
    format to a JWK object, then exports this JWK object to a public key in
    PEM format.

    Args:
        jwk_dict (dict): A dictionary representing the JWK to be converted.

    Returns:
        str: A string representing the Public Key in PEM format.

    Note:
        This function involves using additional cryptography libraries, which
        might not be desirable in some cases due to increased complexity and
        potential security implications. Be sure to validate this approach fits
        into your security requirements before using it.
    """
    jwk_key = jwk.JWK()
    jwk_key.import_key(**jwk_dict)
    public_key = jwk_key.export_to_pem(private_key=False, password=None)
    return public_key.decode()

def get_user_id_from_cookies():
    user_id_cookie = request.cookies.get('user-id')
    if user_id_cookie:
        # Decode the cookie value if necessary
        decoded_user_id = unquote(user_id_cookie).split('|')[0]
        logger.info(f"Decoded user ID: {decoded_user_id}")
        return decoded_user_id
    else:
        logger.warning("user-id cookie not found")
        logger.info(f"All cookies: {request.cookies}")
        return None

def azure_ad_authentication(func):
    def wrapper(*args, **kwargs):
        try:

            if 'user_id' in session:
                # User is already logged in, proceed to the requested page
                return func(*args, **kwargs)
                
            # Check if RStudio user ID is available
            logger.info("Attempting to get RStudio user ID.")
            rstudio_user_id = get_rstudio_user_id()
            if rstudio_user_id:
                # Use the RStudio user ID instead of the OAuth2 token
                request.environ['user_id'] = rstudio_user_id
                logger.info("Set env user_id to {rstudio_user_id}")
                return func(*args, **kwargs)
                
            logger.info("Attempting to get user-id from cookies.")
            logger.info(f"request.cookies:{request.cookies}")
            user_id = get_user_id_from_cookies()
            logger.info(f"user-id from cookies:{user_id}")
            secure = request.scheme == "https"
            
            if not user_id:
                logger.info("Attempting to get id_token from cookies.")
                id_token = request.cookies.get("id_token")
                logger.info(f"id_token from cookies: {id_token}")
                if not id_token:
                    logger.info("Attempting to get Set-Cookie header.")
                    set_cookie_header = request.headers.get("Set-Cookie")
                    logger.info(f"Set-Cookie header: {set_cookie_header}")

                    if set_cookie_header:
                        logger.info("Attempting to extract cookie")
                        id_token_set = extract_id_token(set_cookie_header)
                        logger.info(f"Extracted id_token from Set-Cookie header: {id_token_set}")

                        if id_token_set:
                            id_token = id_token_set

                if not id_token:
                    msg = "No id_token found in request"
                    logger.error(msg)
                    
                    # Redirect to login if no id_token is found
                    try:
                        obj_security_oauth = security_oauth.SecurityOAuth()
                        response_mode = "form_post"
                        logger.info("Initiating redirect to login page.")
                        response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
                        logger.info("Returning login redirect response.")
                        return response
                    except Exception as redirect_ex:
                        logger.error(f"Error during redirection to login: {str(redirect_ex)}")
                        return jsonify({"error": "Redirect to login failed"}), 401

                # Validate the id_token
                logger.info("Validating id_token.")
                decoded_token = validate_id_token(id_token)
                logger.info(f"Decoded id_token: {decoded_token}")


                # Extract user_id from the token
                user_id = decoded_token.get("unique_name")
                logger.info(f"User ID from token: {user_id}")
                original_response = func(*args, **kwargs)
                
                logger.info(f"Request scheme: {request.scheme}, secure: {secure}")
                # Call the original function
                logger.info("Token is valid, calling the original function.")
                flask_response = make_response(original_response)
                logger.info("Original function called successfully.")
                flask_response.set_cookie("id_token", id_token, path="/", secure=secure, httponly=False, samesite="Lax")
                flask_response.headers["Authorization"] = f"Bearer {id_token}"
            else:
                original_response = func(*args, **kwargs)
                flask_response = make_response(original_response)
                logger.info("Original function called successfully.")
            

            
            logger.info("Created Flask response from original response.")

            # Set cookies on the response
            # flask_response.set_cookie("user_id", user_id, secure=secure, samesite="Strict")
            flask_response.set_cookie("user-id", user_id, secure=secure, samesite="Lax")
            flask_response.set_cookie("user_id", user_id, secure=secure, samesite="Lax")

            flask_response.set_cookie("redirect_attempted", "", expires=0, secure=secure, samesite="Strict")

            flask_response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS

            logger.info("Attempting to get id_token from cookies.")
            id_token = request.cookies.get("id_token")
            logger.info(f"id_token from cookies: {id_token}")
            user_id = request.cookies.get("user-id")
            # if user_id:
            #    logger.info(f"user-id cookie is already set: {user-id}")
                # If the user_id is already set, proceed with the original function
            #    return func(*args, **kwargs)
            #else:
            #    logger.info(f"user-id cookie is not already set")


            if not id_token:
                logger.info("Attempting to get Set-Cookie header.")
                set_cookie_header = request.headers.get("Set-Cookie")
                logger.info(f"Set-Cookie header: {set_cookie_header}")

                if set_cookie_header:
                    logger.info("Attempting to extract cookie")
                    id_token_set = extract_id_token(set_cookie_header)
                    logger.info(f"Extracted id_token from Set-Cookie header: {id_token_set}")

                    if id_token_set:
                        id_token = id_token_set

            if not id_token:
                msg = "No id_token found in request"
                logger.error(msg)
                
                # Redirect to login if no id_token is found
                try:
                    obj_security_oauth = security_oauth.SecurityOAuth()
                    response_mode = "form_post"
                    logger.info("Initiating redirect to login page.")
                    response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
                    logger.info("Returning login redirect response.")
                    return response
                except Exception as redirect_ex:
                    logger.error(f"Error during redirection to login: {str(redirect_ex)}")
                    return jsonify({"error": "Redirect to login failed"}), 401
        
            # Validate the id_token
            logger.info("Validating id_token.")
            decoded_token = validate_id_token(id_token)
            logger.info(f"Decoded id_token: {decoded_token}")

            # Call the original function
            logger.info("Token is valid, calling the original function.")
            original_response = func(*args, **kwargs)
            logger.info("Original function called successfully.")

            # Extract user_id from the token
            user_id = decoded_token.get("unique_name")
            logger.info(f"User ID from token: {user_id}")

            secure = request.scheme == "https"
            logger.info(f"Request scheme: {request.scheme}, secure: {secure}")

            flask_response = make_response(original_response)
            logger.info("Created Flask response from original response.")


            # Set cookies on the response
            flask_response.set_cookie("user_id", user_id, secure=secure, samesite="Strict")
            flask_response.set_cookie("user-id", user_id, secure=secure, samesite="Lax")
            flask_response.set_cookie("id_token", id_token, path="/", secure=secure, httponly=False, samesite="Lax")
            flask_response.set_cookie("redirect_attempted", "", expires=0, secure=secure, samesite="Strict")


            flask_response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
            logger.info("Set response headers for CORS and Authorization.")


            return flask_response

        except Exception as ex_not_authenticated:
            full_traceback = traceback.format_exc()  # Get the full traceback
            logger.warning(f"Error: not authenticated: {str(ex_not_authenticated)}")
            logger.warning(f"Full exception details: {full_traceback}")  # Log full exception

            obj_security_oauth = security_oauth.SecurityOAuth()
            response_mode = "form_post"
            response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
            logger.info("Returning login redirect response.")
            return response

    return wrapper

def enforce_https(function_name):
    """
    Decorator function to enforce HTTPS. If a request is made using HTTP,
    it redirects the request to HTTPS.

    Args:
        function_name (function): The Flask view function to decorate.

    Returns:
        function: The decorated function.
    """

    @wraps(function_name)
    def decorated(*args, **kwargs):
        if request.url.startswith("http://"):
            url = request.url.replace("http://", "https://", 1)
            code = 301
            return redirect(url, code=code)
        return function_name(*args, **kwargs)

    return decorated

def get_datetime(entry):
    date_string = entry[0]
    if date_string == "0001-01-01 00:00:00":
        # Handle the specific string and return a valid datetime object
        return datetime.min
    try:
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    except Exception as ex:
        msg = f"Error processing {entry}.  Could not convert '{date_string}' to a datetime object. Please check if it matches the format %Y-%m-%d %H:%M:%S'. Error: {str(ex)}"
        print(msg)

        # return datetime.min to sort invalid dates to the beginning, or datetime.max to sort them to the end
        return datetime.min

@app.route("/cdh_configuration/upload_codes/<data_product_id>")
@azure_ad_authentication
def upload_codes(data_product_id):
    with tracer.start_as_current_span("upload_codes"):
        try:

 
            calling_page_url = request.url
            logger.info(f"Full request URL: {request.url}")

            logger.info(f"data_product_id: {data_product_id}")

            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Go up one directory from the current directory
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
            # Construct the relative path to the CSV file
            if parent_dir   is None:
                raise ValueError("parent_dir is None, cannot construct path.")
            if data_product_id   is None:
                raise ValueError("data_product_id is None, cannot construct path.")
            csv_directory_path = os.path.join(parent_dir, data_product_id,"config")
            csv_path = os.path.join(parent_dir, data_product_id,"config", "bronze_sps_config_jobs.csv")
            logger.info(f"csv_path:{csv_path}")
            df = pd.read_csv(csv_path)
            # Convert the DataFrame to a list of dictionaries
            data = df.to_dict(orient="records")
            environments = list_config_environments(csv_directory_path)

            
            
            print(f"data_product_id: {data_product_id}")  # Debugging line
            return render_template(
                "data_products/upload_codes.html",
                data_product_id=data_product_id,
                calling_page_url=calling_page_url,
                environments=environments,
            )
        except Exception as ex:
            trace_msg_error = traceback.format_exc()
            line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
            error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg_error}"
            exc_info = sys.exc_info()
            # logger_singleton.error_with_exception(error_message, exc_info)
            return render_template("error.html", error_message=error_message)



@app.route("/synthea/")
def home():
    return render_template("synthea/synthea_home.html")

@app.route("/synthea/generate")
def generate():
    
    # Assuming you have a DataFrame with Synthea module names
    df_synthea_modules = pd.DataFrame({
        'synthea_module_names': ['Module1', 'Module2', 'Module3', 'Module4']
    })
    synthea_module_names = df_synthea_modules['synthea_module_names'].tolist()
    return render_template("synthea/synthea_generate.html", synthea_module_names=synthea_module_names)

@app.route("/synthea/visualize")
def visualize():
    return render_template("synthea/synthea_visualize.html")


@app.route("/synthea/generate", methods=["POST"])
def generate_data():
    data = request.get_json()
    patient_count = data.get("patientCount")
    # Assuming Synthea is set up to be called via a subprocess
    result = subprocess.run(["./run_synthea", "-p", patient_count], capture_output=True)
    if result.returncode == 0:
        return jsonify(count=patient_count)
    else:
        return jsonify(error="Failed to generate data"), 500


@app.route("/")
def index():
    return render_template("index.html")


@cdc_files_bp.route("/download_edc")
def download_edc():
    calling_page_url = request.args.get("calling_page")
    return render_template("download_edc.html", calling_page_url=calling_page_url)


@cdc_files_bp.route("/download_codes")
def download_codes():
    calling_page_url = request.args.get("calling_page")
    return render_template("download_codes.html", calling_page_url=calling_page_url)


@cdc_files_bp.route("/reports")
def reports():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one directory from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Construct the relative path to the CSV file
    csv_path = os.path.join(parent_dir, "lava_core", "bronze_reports.csv")

    df = pd.read_csv(csv_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient="records")

    calling_page_url = request.args.get("calling_page")
    return render_template(
        "reports/reports_home.html", calling_page_url=calling_page_url, data=data
    )


@cdc_files_bp.route("/dashboards")
def dashboards():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one directory from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Construct the relative path to the CSV file
    csv_path = os.path.join(parent_dir, "lava_core", "bronze_dashboards.csv")

    df = pd.read_csv(csv_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient="records")

    calling_page_url = request.args.get("calling_page")
    return render_template(
        "dashboards/dashboards_home.html", calling_page_url=calling_page_url, data=data
    )

 
class DependencyGraph(Resource):
 
    def get(self, operation_id, data_product_id, environment, page):

        items_per_page = 10  # You can adjust this or make it configurable

        tracer_singleton = TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        )

        with tracer.start_as_current_span("dependency_graph"):
            try:
                logger.info(f"navigating to page: {page}")
                current_dir = os.path.dirname(__file__)

                dotenv_path = os.path.join(os.path.dirname(current_dir), "lava_core", ".env")
                if not os.path.exists(dotenv_path):
                    dotenv_path = os.path.join(os.path.dirname(current_dir), ".env")

                load_dotenv(dotenv_path)
                
                obj_az_kql = AzKql()
                chart_html = obj_az_kql.graph_ai_dependencies(operation_id, data_product_id, environment, page, items_per_page)
                calling_page_url = request.args.get("calling_page")

                tracer_singleton.force_flush()
                html_content = render_template(
                    "dashboards/dependency_graph.html", 
                    calling_page_url=calling_page_url, 
                    chart=chart_html, 
                    operation_id=operation_id
                )
                response = make_response(html_content)
                response.headers['Content-Type'] = 'text/html'
                return response

            except Exception as ex:
                trace_msg = traceback.format_exc()
                line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
                error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
                exc_info = sys.exc_info()
                html_content =  render_template("error.html", error_message=error_message)
                response = make_response(html_content)
                response.headers['Content-Type'] = 'text/html'
                return response

@cdc_modules_bp.route("/module/<module_name>")
def module(module_name):
    data = {}
    # Implement the logic to display the module based on the module_name
    calling_page_url = request.args.get("calling_page")
    module_name = module_name.lower()
    return render_template(
        f"{module_name}/{module_name}_home.html",
        calling_page_url=calling_page_url,
        data=data,
    )


@cdc_modules_bp.route("/modules")
def modules():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one directory from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Construct the relative path to the CSV file
    csv_path = os.path.join(parent_dir, "lava_core", "bronze_modules.csv")

    df = pd.read_csv(csv_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient="records")

    calling_page_url = request.args.get("calling_page")
    return render_template(
        "modules/modules_home.html", data=data, calling_page_url=calling_page_url
    )


@cdc_files_bp.route("/data_product_job/<data_product_id>")
def data_product_job(data_product_id):

    tracer, logger = LoggerSingleton.instance(
        NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
    ).initialize_logging_and_tracing()

    with tracer.start_as_current_span("data_product_job"):
        try:

            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Go up one directory from the current directory
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

            # Construct the relative path to the CSV file
            csv_directory_path = os.path.join(parent_dir, data_product_id,"config")
            csv_path = os.path.join(parent_dir, data_product_id,"config", "bronze_sps_config_jobs.csv")
            logger.info(f"csv_path:{csv_path}")
            df = pd.read_csv(csv_path)
            # Convert the DataFrame to a list of dictionaries
            data = df.to_dict(orient="records")
            jobs = []
            for row in data:
                jobs.append(row['job'])  # Extract the 'job' field
            calling_page_url = request.url
            environments = list_config_environments(csv_directory_path)
            return render_template(
                "data_products/data_product_job.html", calling_page_url=calling_page_url, jobs=jobs, environments=environments
            )
        except Exception as ex:
            trace_msg = traceback.format_exc()
            line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
            error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
            exc_info = sys.exc_info()
            # logger_singleton.error_with_exception(error_message, exc_info)
            return render_template("error.html", error_message=error_message)


@cdc_files_bp.route("/data_products")
def data_products():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one directory from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Construct the relative path to the CSV file
    csv_path = os.path.join(parent_dir, "lava_core", "bronze_data_products.csv")

    df = pd.read_csv(csv_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient="records")

    calling_page_url = request.args.get("calling_page")
    return render_template(
        "data_products/data_products_home.html",
        calling_page_url=calling_page_url,
        data=data,
    )


@cdc_files_protected_bp.route("/upload_edc")
def upload_edc():
    calling_page_url = request.args.get("calling_page")
    return render_template("data_products/upload_edc.html", calling_page_url=calling_page_url)


@cdc_admin_bp.route("/error")
def error():
    error_message = "An unexpected error occurred"
    return render_template("error.html", error_message=error_message, error_url="")


@cdc_admin_bp.route("/get_log_file_tail/<int:number_of_lines>")
def get_log_file_tail(number_of_lines):
    """
    Retrieves the tail of a log file and renders it in an HTML template.

    Args:
        number_of_lines (int): The number of lines to retrieve from the log file.

    Returns:
        str: The rendered HTML template containing the log file entries.

    Raises:
        Exception: If an internal server error occurs while fetching the log file.
        ValueError: If the log data is None, or if the number_of_lines is missing or blank.
    """

    tracer, logger = LoggerSingleton.instance(
        NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
    ).initialize_logging_and_tracing()

    with tracer.start_as_current_span("get_log_file_tail"):
        try:
            log_data = None

            (
                status_code,
                number_of_lines,
                log_data,
            ) = LoggerSingleton.instance(
                NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
            ).get_log_file_tail(number_of_lines)
            if status_code == 500:
                error_msg = f"Internal Server Error fetching log file: The server encountered an error. {log_data}"
                raise Exception(error_msg)

            if log_data is None:
                raise ValueError(
                    f"Internal Server Error fetching log file: Log data is None. {log_data}"
                )

            if number_of_lines is None or number_of_lines == 0:
                raise ValueError(
                    "Internal Server Error fetching log file: number_of_lines is missing or blank"
                )

            log_entries = []

            for line_number, line in enumerate(log_data.strip().split("\n"), start=1):
                log_entries.append(line.split("\u001F"))

            for entry in log_entries:
                try:
                    asctime, name, module, lineno, levelname, message = entry
                    datetime_object = datetime.strptime(asctime, "%Y-%m-%d %H:%M:%S")
                    asctime = datetime_object.strftime("%Y-%m-%d %I:%M:%S %p")
                    entry = [asctime, name, module, lineno, levelname, message]
                except ValueError as ex:
                    logger.warning(f"Error parsing line: {str(ex)}")
                except IndexError:
                    logger.warning(f"Error: line has missing fields: {entry}")

            # Sort log_entries by date and time in descending order
            log_entries.sort(key=lambda entry: get_datetime(entry), reverse=True)

            return render_template("log_file.html", entries=log_entries)

        except Exception as ex:
            trace_msg = traceback.format_exc()
            line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
            error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
            exc_info = sys.exc_info()
            # logger_singleton.error_with_exception(error_message, exc_info)
            return render_template("error.html", error_message=error_message)


app.register_blueprint(cdc_admin_bp)
app.register_blueprint(cdc_files_bp)
app.register_blueprint(cdc_files_protected_bp)
app.register_blueprint(altmetric_bp)
app.register_blueprint(cdc_modules_bp)

metric_exporter = AzureMonitorMetricExporter()

logger = app.logger
tracer = app.tracer

FlaskInstrumentor().instrument_app(app)

if ENVIRONMENT == "prod":
    INSTRUMENTATION_KEY = "e7808e07-4242-4ed3-908e-c0a4c3b719b1"
else:
    INSTRUMENTATION_KEY = "8f02ef9a-cd94-48cf-895a-367f102e8a24"

if INSTRUMENTATION_KEY is None:
    raise ValueError("APPLICATIONINSIGHTS_INSTRUMENTATION_KEY environment variable is not set")

# Set up metrics exporter (optional)
metrics_exporter = AzureMonitorMetricExporter(
    connection_string=f"InstrumentationKey={INSTRUMENTATION_KEY}"
)
# Set up the metric reader and provider
metric_reader = PeriodicExportingMetricReader(metrics_exporter)
meter_provider = MeterProvider(metric_readers=[metric_reader])

# Set the meter provider globally
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# Create a counter for availability monitoring
availability_counter = meter.create_counter(
    name="website_availability",
    unit="1",
    description="Counts availability checks for the website"
)

 
obj_tracer_singleton = TracerSingleton.instance(
    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
)


API_DESCRIPTION = """
<h2>API Documentation</h2>
<p>CDC Data Hub LAVA (CDH) provides shared resources,
practices and guardrails for analysts to discover, access, link, and use
agency data in a consistent way. CDH improvements in standardized and 
streamlined workflows reduce the effort required to find, access, and
trust data.</p>
<p><a href="/">Back to Home</a></p>
<p><a href="../files/upload_codes?data_product_id=premier_respiratory">Config Upload Page</a></p>
<p><a href="../files/download_codes">Config Download Page</a></p>
<p><a href="../protected_files/upload_edc">EDC Upload Page</a></p>
<p><a href="../files/download_edc">EDC Download Page</a></p>
<p>For detailed logs, please visit the <a href="../logs/get_log_file_tail/1000">Log File Page</a>.</p>
"""

(
    api,
    ns_welcome,
    ns_alation,
    ns_jira,
    ns_posit,
    ns_cdc_admin,
    ns_cdh_security,
    ns_altmetric,
    ns_cdh_orchestration,
    ns_cdh_configuration,
    ns_cdh_observability
) = create_api(app, API_DESCRIPTION)

# Set Azure AD credentials using DefaultAzureCredential
azure_credential = DefaultAzureCredential()

# Define a model for the metadata
metadata_model = api.model(
    "Metadata",
    {
        "start_time": fields.Float,
        "end_time": fields.Float,
        "total_time": fields.Float,
        "data": fields.String,
    },
)

# Define the file link model
file_link_model = api.model(
    "FileLink",
    {"link": fields.String(description="Download link for the metadata file")},
)


def get_posit_api_key():
    with tracer.start_as_current_span(f"get_posit_api_key"):
        config = app.cdc_config
        data_product_id = config.get("data_product_id")
        environment = config.get("environment")
        posit_connect_base_url = config.get("posit_connect_base_url")

        logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
        az_sub_web_client_secret_key = config.get("az_sub_web_client_secret_key")
        az_sub_web_oauth_secret_key = config.get("az_sub_web_oauth_secret_key")
        az_sub_web_oauth_secret_key = az_sub_web_oauth_secret_key.replace("-", "_")
        az_sub_web_oauth_secret_key = az_sub_web_oauth_secret_key.upper()
        client_secret = os.getenv(az_sub_web_oauth_secret_key)
        tenant_id = config.get("az_sub_tenant_id")
        client_id = config.get("az_sub_client_id")
        az_kv_key_vault_name = config.get("az_kv_key_vault_name")
        running_interactive = False
        if not client_secret:
            running_interactive = True

        az_key_vault = cdh_az_key_vault.AzKeyVault(
            tenant_id,
            client_id,
            client_secret,
            az_kv_key_vault_name,
            running_interactive,
            data_product_id,
            environment,
            az_sub_web_client_secret_key,
        )

        az_kv_posit_connect_secret_key = config.get("az_kv_posit_connect_secret_key")

        cdh_databricks_kv_scope = config.get("cdh_databricks_kv_scope")

        az_kv_posit_connect_secret = az_key_vault.get_secret(
            az_kv_posit_connect_secret_key, cdh_databricks_kv_scope
        )

        return az_kv_posit_connect_secret



def validate_id_token(id_token):
    """
    Validates an ID token received from Azure Active Directory (Azure AD).

    This function retrieves the OpenID Connect metadata document for the tenant,
    obtains the JSON Web Key Set (JWKS), locates the signing key matching the `kid` (Key ID) in the token header,
    and then decodes and verifies the ID token using the found key.

    Parameters:
    id_token (str): The ID token to validate.

    Returns:
    dict: The decoded ID token if the token is valid.

    Raises:
    ValueError: If unable to find the signing key for the token.

    Note:
    This function performs basic ID token validation which includes signature verification,
    and checking of the audience ('aud') claim. Depending on the requirements of your application,
    you might need to perform additional validation, such as checking the issuer ('iss') claim,
    token expiration, etc.

    Ensure that your Azure AD tenant, client ID and client secret are correctly set in your application configuration.

    """

    config = app.cdc_config
    tenant_id = config.get("az_sub_tenant_id")
    client_id = config.get("az_sub_client_id")

    # Get the OpenID Connect metadata document
    openid_config_url = f"https://login.microsoftonline.com/{tenant_id}/v2.0/.well-known/openid-configuration"
    openid_config_response = requests.get(openid_config_url)
    openid_config = openid_config_response.json()

    # Decode the token header without validation to get the kid
    token_header = jwt.get_unverified_header(id_token)
    kid = token_header["kid"]

    # Get the signing keys
    jwks_url = openid_config["jwks_uri"]
    jwks_response = requests.get(jwks_url)
    jwks = jwks_response.json()

    # Find the key with the matching kid
    key = next((k for k in jwks["keys"] if k["kid"] == kid), None)
    if key is None:
        raise ValueError("Unable to find the signing key for the token.")

    # Use the function
    public_key = jwk_to_pem(key)

    # Validate the token
    try:
        # Decode the JWT without verification
        decoded_token = jwt.decode(id_token, options={"verify_signature": False})

        # Todo add back signature verificaiton
        # decoded_token = jwt.decode(id_token, public_key, algorithms=["RS256"], audience=client_id)

        return decoded_token

    except Exception as ex:
        error_msg = f"Error in token valiation: {str(ex)}."
        exc_info = sys.exc_info()
        print(error_msg)
        raise


def handle_redirect():
    # Attempt to get the redirect_url from query parameters
    redirect_url = request.args.get("redirect_url")
    
    # Check if redirect_url is empty
    if not redirect_url:
        # Attempt to get the X-Rstudio-Session-Original-Uri header as a fallback
        redirect_url = request.headers.get('X-Rstudio-Session-Original-Uri')
        logger.info(f"Using X-Rstudio-Session-Original-Uri header for redirect: {redirect_url}")
    
    # Final fallback to the index page if both are empty
    if not redirect_url:
        redirect_url = url_for('index')
        logger.info(f"No redirect URL found, defaulting to index page: {redirect_url}")
    
    # Log the final redirect URL
    logger.info(f"Final redirect URL: {redirect_url}")

    # Perform the redirect
    return redirect(redirect_url)
    

class AuthCallback(Resource):
    @api.expect(auth_parser, validate=True)
    def get(self):
        """
        Handle the process after receiving an authorization code from an authentication callback.
        Represents part 2 of the code flow to retrieve an ID token.  This part retrieves the id_token and user_id from the authorization code.

        Steps:
        1. Extract the 'code' and 'state' parameters from the request.
        2. If 'code' is not found and no redirection attempt has been made, a login redirect response is initiated.
        3. If 'state' is missing, a 400 error response is returned.
        4. Decode the 'state' from a Base64 encoded string to a dictionary.
        5. Get an ID token using the authorization code.
        6. If the ID token is valid, decode the JWT to get user details, set cookies, set headers and redirect the user.
        7. In case of any error during JWT decoding, a 400 error response is returned.
        8. If the ID token is invalid and no redirection attempt has been made, a login redirect response is initiated.

        Returns:
            Response: A flask response object that could be a redirect or an error message.

        Raises:
            Exception: If there's an error in decoding the JWT.

        Notes:
            - Commented out lines represent an alternative flow to handle redirection attempts.
            - It's expected that `ALLOWED_ORIGINS` is a globally defined list of allowed origins.
            - This function relies on several external methods/functions such as `get_login_redirect_response`,
            `make_response`, `redirect`, and `get_id_token_from_auth_code`.
        """

        # Check if running inside RStudio Connect
        rstudio_user_id = get_rstudio_user_id()
        if rstudio_user_id:
            # Set the user_id in the environment
            logger.info(f"RS_SERVER_URL found, user-id extracted: {rstudio_user_id}")
            request.environ['user_id'] = rstudio_user_id
            
            # Redirect to the desired URL or handle the user session as needed
            response = make_response(handle_redirect())

            logger.info(f"Setting user_id cookie: {rstudio_user_id}")
            response.set_cookie("user_id", rstudio_user_id, secure=True, samesite="Strict")
            return response

        url_with_error = request.url

        # Get the authorization code from the response
        args = auth_parser.parse_args()
        auth_code = args["code"]

        # Check if we've tried redirecting before
        if auth_code is None:
            # redirect_attempted = request.args.get("redirect_attempted")

            # if not redirect_attempted:
            # Mark that we've tried redirecting
            obj_security_oauth = security_oauth.SecurityOAuth()
            response_mode = "form_post"
            # response_mode = "query"
            config = app.cdc_config
            response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
            return response
            # else:
            #    msg = "Authorization code missing after redirect attempt."
            #    return make_response(msg, 400)

        # Get the   state from the response
        state = args["state"]

        if state is None:
            msg = f"Missing state parameter in url {url_with_error}"
            response = make_response(msg, 400)

            return response

        base64_string = state

        # Get the redirect_url from the query parameters and unquote it
        # redirect_url = unquote(request.args.get('redirect_url'))
        # Base64 decode the string
        decoded_bytes = base64.urlsafe_b64decode(base64_string)

        # Decode the bytes to a string
        decoded_string = decoded_bytes.decode("utf-8")

        # URL decode the string
        url_decoded_string = unquote(decoded_string)

        # Convert the string to a dictionary
        data = ast.literal_eval(url_decoded_string)

        # Load the JSON data
        url = data.get("url")
        current_url = request.url
        redirect_url = current_url
        
        config = app.cdc_config
        data_product_id = config.get("data_product_id")
        environment = config.get("environment")

        obj_security_oauth = security_oauth.SecurityOAuth()
        id_token = obj_security_oauth.get_id_token_from_auth_code(auth_code, config, data_product_id, environment, code_verifier)

        if id_token and "." in id_token and id_token.count(".") >= 2:
            try:
                # Decode the JWT without verification
                decoded_token = jwt.decode(
                    id_token, options={"verify_signature": False}
                )

                # Now you can access claims in the token, like the user's ID
                # 'oid' stands for Object ID
                user_id = decoded_token.get("unique_name")

                # Make a response object that includes a redirect
                response = make_response(redirect(url))

                secure = request.scheme == "https"
                logger.info(f"secure: {secure}")

                response.set_cookie(
                    "redirect_attempted",
                    "",
                    expires=0,
                    secure=secure,
                    samesite="Strict",
                )
                response.set_cookie(
                    "user_id", user_id, secure=secure, samesite="Strict"
                )
                response.set_cookie(
                    "id_token",
                    id_token,
                    path="/",
                    secure=secure,
                    httponly=False,
                    samesite="Lax",
                )

                response.headers["Authorization"] = f"Bearer {id_token}"
                response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
                # Redirect the user to the home page, or wherever they should go next
                return response

            except Exception as ex:
                print(ex)
                msg = "Error in decoding id_token: str(ex)"
                response = make_response(msg, 400)

        else:
            error_code = check_and_return_error(id_token)
            error_message = f"Invalid id_token after redirect attempt. id_token error_code: {error_code}"
            print(error_message)
            # redirect_attempted = request.args.get("redirect_attempted")
            # if not redirect_attempted:
            # Mark that we've tried redirecting
            if error_code == "":
                obj_security_oauth = security_oauth.SecurityOAuth()
                # response_mode = "form_post"
                response_mode = "query"
                response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
                return response
            else:
                # Generate the content using render_template
                content = {"error": error_message}
                # Create a response object using make_response
                response = make_response(content, 500)

                # Return the customized response object
                return response

    @api.expect(auth_form_parser, validate=False)
    def post(self):
        """
        Handle the POST request after receiving an authorization code from an authentication callback.
        Represents part 1 of the code flow to retrieve an ID token.  This part retrieves the authorization code.
        The code completes a POST as opposed to a GET to prevent an error with excessive length in the query string from Azure.

        Steps:
        1. Extract the 'code' and 'state' parameters from the request.
        2. If the 'code' is missing:
        - If a redirection hasn't been attempted yet, set a "redirect_attempted" cookie and initiate a login redirect.
        - If a redirection was already attempted, return a 400 error and clear the "redirect_attempted" cookie.
        3. If the 'state' is missing, return a 400 error and clear the "redirect_attempted" cookie.
        4. Decode the 'state' from a Base64 encoded string to a dictionary.
        5. Get an ID token using the authorization code.
        6. If the ID token is valid:
        - Decode the JWT to retrieve user details.
        - Set relevant cookies and headers, and redirect the user.
        7. If the ID token is invalid:
        - If a redirection hasn't been attempted yet, set a "redirect_attempted" cookie and initiate a login redirect.
        - If a redirection was already attempted, return a 400 error and clear the "redirect_attempted" cookie.

        Returns:
            Response: A Flask response object that could be a redirect or an error message.

        Raises:
            Exception: If there's an error in decoding the JWT.

        Notes:
        - This function checks if the request is over HTTPS to set the "secure" attribute for cookies.
        - The "redirect_attempted" cookie expires in 10 minutes if set.
        - Commented out lines represent potential alternative code paths.
        - This function relies on several external methods/functions such as `get_login_redirect_response`,
            `make_response`, `redirect`, and `get_id_token_from_auth_code`.
        - It's expected that `ALLOWED_ORIGINS` is a globally defined list of allowed origins.
        """

        try:
            url_with_error = request.url
            logger.info(f"Request URL with error: {url_with_error}")

            # Get the authorization code from the response
            logger.info("Parsing authorization code from the response.")
            args = auth_form_parser.parse_args()

            # Get the authorization code and state from the parsed arguments
            auth_code = args.get("code")
            state = args.get("state")

            # Check if we've tried redirecting before
            if auth_code is None:
                return "Success 1079"
                if not request.cookies.get("redirect_attempted"):
                    return "Success 1080"
                    # Mark that we've tried redirecting
                    logger.info("No authorization code found and redirect not attempted before. Redirecting for login.")
                    obj_security_oauth = security_oauth.SecurityOAuth()
                    response_mode = "form_post"
                    config = app.cdc_config
                    response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
                    response.set_cookie(
                        "redirect_attempted",
                        "true",
                        max_age=600,
                        secure=(request.scheme == "https"),
                        samesite="Strict",
                    )
                    return response
                else:
                    return "Success 1095"
                    msg = "Authorization code missing after redirect attempt."
                    logger.error(msg)
                    response = jsonify({"error": msg})
                    response.status_code = 400
                    response.set_cookie(
                        "redirect_attempted",
                        "",
                        expires=0,
                        secure=(request.scheme == "https"),
                        samesite="Strict",
                    )
                    return response
        
            if state is None:
                return "Success 1111"
                msg = f"Missing state parameter in url {url_with_error}"
                logger.error(msg)
                response = jsonify({"error": msg})
                response.status_code = 400
                response.set_cookie(
                    "redirect_attempted",
                    "",
                    expires=0,
                    secure=(request.scheme == "https"),
                    samesite="Strict",
                )
                return response

            base64_string = state
            decoded_bytes = base64.urlsafe_b64decode(base64_string)
            decoded_string = decoded_bytes.decode("utf-8")
            url_decoded_string = unquote(decoded_string)
            data = ast.literal_eval(url_decoded_string)

            data_url = data.get("url")
            current_url = request.url
            location_url = request.headers.get("Location")

            urls = [data_url, location_url, current_url]
            redirect_url = next(
                (url for url in urls if url and "cdh_security/callback" not in url),
                None,
            )

            obj_security_oauth = security_oauth.SecurityOAuth()
            config = app.cdc_config
            data_product_id = config.get("data_product_id")
            environment = config.get("environment")
            id_token = obj_security_oauth.get_id_token_from_auth_code(auth_code, config, data_product_id, environment, code_verifier)

            if id_token and "." in id_token and id_token.count(".") >= 2:
                try:
                    decoded_token = jwt.decode(
                        id_token, options={"verify_signature": False}
                    )
                    user_id = decoded_token.get("unique_name")

                    response = make_response(redirect(redirect_url))
                    secure = request.scheme == "https"

                    response.set_cookie(
                        "redirect_attempted",
                        "",
                        expires=0,
                        secure=secure,
                        samesite="Strict",
                    )
                    response.set_cookie(
                        "user_id", user_id, secure=secure, samesite="Strict"
                    )
                    response.set_cookie(
                        "id_token",
                        id_token,
                        path="/",
                        secure=secure,
                        httponly=False,
                        samesite="Lax",
                    )

                    response.headers["Authorization"] = f"Bearer {id_token}"
                    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
                    return response

                except jwt.ExpiredSignatureError:
                    return jsonify({"message": "ID token has expired."}), 401

                except jwt.InvalidTokenError:
                    return jsonify({"message": "Invalid ID token."}), 401

                except Exception as ex:
                    logger.error(f"Error in decoding ID token: {str(ex)}")
                    response = jsonify({"message": f"Error in decoding ID token: {str(ex)}"})
                    response.status_code = 502
                    response.set_cookie(
                        "redirect_attempted",
                        "",
                        expires=0,
                        secure=(request.scheme == "https"),
                        samesite="Strict",
                    )
                    return response

            else:
                error_code = check_and_return_error(id_token)
                msg = f"Invalid id_token after redirect attempt. id_token error_code: {error_code}"
                logger.error(msg)
                if not request.cookies.get("redirect_attempted"):
                    obj_security_oauth = security_oauth.SecurityOAuth()
                    response_mode = "form_post"
                    response = obj_security_oauth.get_login_redirect_response(config, response_mode, DATA_PRODUCT_ID, ENVIRONMENT, code_verifier)
                    response.set_cookie(
                        "redirect_attempted",
                        "true",
                        max_age=600,
                        secure=(request.scheme == "https"),
                        samesite="Strict",
                    )
                    return response
                else:
                    response = jsonify({"error": msg})
                    response.status_code = 500
                    response.set_cookie(
                        "redirect_attempted",
                        "",
                        expires=0,
                        secure=(request.scheme == "https"),
                        samesite="Strict",
                    )
                    return response
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return jsonify({"status": "error", "message": str(e)}), 500




class AltmetricDownload(Resource):
    """
    Represents a resource for downloading Altmetric data.
    """

    def get(self, altmetric_id=None):
        """
        Handles the GET request for downloading Altmetric data.

        Parameters:
            altmetric_id: Altmetric number used to retrieve document metadata. (Example: 149664243)

        Returns:
            A JSON response containing the downloaded Altmetric data, or an error message if the download_edc fails.
        """

        args = parser.parse_args()
        data_product_id = args[
            "data_product_id"
        ]  # Default value is handled by the parser
        environment = args["environment"]  # Default value is handled by the parser

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("__init__"):
            try:
                if not altmetric_id:
                    return jsonify({"error": "altmetric_id parameter is required"}), 400

                if not data_product_id:
                    return (
                        jsonify({"error": "data_product_id parameter is required"}),
                        400,
                    )

                obj_altmetric_downloader = AltmetricDownloader()
                results = obj_altmetric_downloader.download_altmetric_data(
                    altmetric_id, data_product_id, environment
                )

                if results is None:
                    return (
                        jsonify({"error": "Failed to download_edc Altmetric data"}),
                        500,
                    )

                return jsonify(results)

            except Exception as ex:
                trace_msg = traceback.format_exc()
                line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
                error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(error_message, exc_info)
                return render_template("error.html", error_message=error_message)


class WelcomeSwagger(Resource):
    def get(self):
        """
        Returns the Swagger API documentation.

        Returns:
            dict: The Swagger API documentation schema.
        """
        with tracer.start_as_current_span("/api/swagger"):
            return api.__schema__


class Issue(Resource):
    """
    Represents the endpoint for retrieving an issue related to a specific project.

    This class is used as a Flask-RESTful resource to handle requests related
    to retrieving a specific issue for a specific JIRA project.

    Args:
        Resource (type): The base class for implementing Flask-RESTful
        resources.


    Attributes:
        jira_project (str): The name or identifier of the project associated with
        the issue.
    """

    def get(self, jira_project=None, jira_issue_id=None, jira_fields=None):
        """
        Retrieves issue associated with a specific project from JIRA.

        Args:
            jira_project (str): The name or identifier of the project. If
                                not provided, retrieves issues for the default project.
            jira_issue_id (str): The identifier of the issue. If provided,
                                the method will retrieve this specific issue.
            jira_fields (str): Comma-separated string of fields to retrieve
                            for the issue(s). If not provided, defaults to
                            "summary,status,assignee".
        Returns:
            dict: A dictionary containing the retrieved issue.

        Note:
            This method communicates with JIRA to fetch the issue.

        Example: LAVA

        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span(f"issue/{jira_project}"):
            try:
                config = app.cdc_config

                cdh_databricks_kv_scope = config.get("cdh_databricks_kv_scope")

                az_kv_key_vault_name = config.get("az_kv_key_vault_name")
                data_product_id = "lava_core"
                environment = "dev"
                client_secret = config.get("client_secret")
                tenant_id = config.get("az_sub_tenant_id")
                client_id = config.get("az_sub_client_id")
                az_kv_key_vault_name = config.get("az_kv_key_vault_name")
                running_interactive = False
                if not client_secret:
                    running_interactive = True

                az_sub_web_client_secret_key = config.get(
                    "az_sub_web_client_secret_key"
                )
                obj_az_keyvault = cdh_az_key_vault.AzKeyVault(
                    tenant_id,
                    client_id,
                    client_secret,
                    az_kv_key_vault_name,
                    running_interactive,
                    data_product_id,
                    environment,
                    az_sub_web_client_secret_key,
                )

                jira_client_secret_key = config.get("jira_client_secret_key")
                jira_client_secret = obj_az_keyvault.get_secret(
                    jira_client_secret_key, cdh_databricks_kv_scope
                )
                if jira_client_secret is None:
                    raise Exception(
                        f"Unable to get Jira client secret from key_vault {jira_client_secret_key}"
                    )
                else:
                    logger.info(f"jira_client_secret_length:{len(jira_client_secret)}")
                    logger.info(
                        f"jira_client_secret_length:{str(len(jira_client_secret))}"
                    )

                if jira_project is None:
                    jira_project = "LAVA"  # Set your default jira_project value here

                jira_base_url = config.get("jira_base_url")
                jira_base_url = jira_base_url.rstrip("/")

                headers = {
                    "Authorization": f"Basic {jira_client_secret}",
                    "Content-Type": "application/json",
                }
                logger.info(f"headers:{headers}")

                params = {
                    "jql": f"project = {jira_project}",
                    "fields": ["summary", "status", "assignee"],
                }

                logger.info(f"Retrieving issue for project {jira_project}")
                logger.info(f"params: {params}")

                jira_client_instance = jira_client.JiraClient()
                jira_issue = jira_client_instance.get_issue(
                    jira_project,
                    headers,
                    jira_base_url,
                    jira_issue_id,
                    jira_fields,
                    data_product_id,
                    environment,
                )

                logger.info(jira_issue)

                return jira_issue

            except Exception as ex:
                msg = f"An unexpected error occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
                ).force_flush()
                return {"error": f"An unexpected error occurred: {msg}"}


class Task(Resource):
    """
    Represents the endpoint for retrieving tasks related to a specific project.

    This class is used as a Flask-RESTful resource to handle requests related
    to retrieving tasks for a specific JIRA project.

    Args:
        Resource (type): The base class for implementing Flask-RESTful
        resources.

    Attributes:
        jira_project (str): The name or identifier of the project associated with
        the tasks.
    """

    def get(self, jira_project=None, jira_component=None, jira_fields=None):
        """
        Retrieves tasks associated with a specific project from JIRA.

        Args:
            jira_project (str, optional): The name or identifier of the project. If
            not provided, retrieves tasks for all projects. Example: LAVA
            jira_component (str): Example: CDH-Premier-Respiratory
            jira_fields (str):  Default to None

        Returns:
            dict: A dictionary containing the retrieved tasks.

        Note:
            This method communicates with JIRA to fetch the tasks.

        Example: LAVA

        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span(f"tasks/{jira_project}"):
            try:
                config = app.cdc_config
                cdh_databricks_kv_scope = config.get("cdh_databricks_kv_scope")
                az_kv_key_vault_name = config.get("az_kv_key_vault_name")
                data_product_id = "lava_core"
                environment = "dev"
                client_secret = config.get("client_secret")
                tenant_id = config.get("az_sub_tenant_id")
                client_id = config.get("az_sub_client_id")
                az_kv_key_vault_name = config.get("az_kv_key_vault_name")
                running_interactive = False
                if not client_secret:
                    running_interactive = True

                az_sub_web_client_secret_key = config.get(
                    "az_sub_web_client_secret_key"
                )
                obj_az_keyvault = cdh_az_key_vault.AzKeyVault(
                    tenant_id,
                    client_id,
                    client_secret,
                    az_kv_key_vault_name,
                    running_interactive,
                    data_product_id,
                    environment,
                    az_sub_web_client_secret_key,
                )

                jira_client_secret_key = config.get("jira_client_secret_key")
                jira_client_secret = obj_az_keyvault.get_secret(
                    jira_client_secret_key, cdh_databricks_kv_scope
                )
                if jira_client_secret is None:
                    raise Exception(
                        f"Unable to get Jira client secret from key_vault {jira_client_secret_key}"
                    )
                else:
                    logger.info(f"jira_client_secret_length:{len(jira_client_secret)}")
                    logger.info(
                        f"jira_client_secret_length:{str(len(jira_client_secret))}"
                    )

                if jira_project is None:
                    jira_project = "LAVA"  # Set your default jira_project value here

                jira_base_url = config.get("jira_base_url")
                jira_base_url = jira_base_url.rstrip("/")

                headers = {
                    "Authorization": f"Basic {jira_client_secret}",
                    "Content-Type": "application/json",
                }
                logger.info(f"headers:{headers}")
                logger.info(f"Retrieving tasks for project {jira_project}")

                jira_client_instance = jira_client.JiraClient()
                jira_tasks = jira_client_instance.get_tasks(
                    jira_project,
                    headers,
                    jira_base_url,
                    jira_component,
                    jira_fields,
                    data_product_id,
                    environment,
                )

                logger.info(jira_tasks)
                return jira_tasks

            except Exception as ex:
                msg = f"An unexpected error occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
                ).force_flush()
                return {"error": f"An unexpected error occurred: {msg}"}


class MetadataJsonFileDownload(Resource):
    """
    A Flask-RESTful resource responsible for downloading metadata JSON files.

    This class handles HTTP requests to the corresponding endpoint. It likely
    implements methods such as GET to handle the downloading of a metadata
    JSON file. Each method corresponds to a standard HTTP method
    (e.g., GET, POST, PUT, DELETE) and carries out a specific operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.
    """

    def get(self, schema_id):
        """
        Retrieves the JSON metadata file from Alation based on the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            JSON file.

        Returns:
            dict: A dictionary containing the downloaded JSON metadata file.

        Example:
            Use schema_id 106788 to test LAVA_CORE_PROD (DataBricks): lava_core_prod
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alation
        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("metadata_json_file_download"):
            try:
                start_time = time.time()  # Record the start time

                config = app.cdc_config

                schema = alation_schema.Schema()
                manifest_json_file = schema.download_manifest_json(schema_id, config)

                # Return the file as a download_edc
                file_name = os.path.basename(manifest_json_file)

                end_time = time.time()  # Record the start time

                total_time = end_time - start_time  # Calculate the total time

                logger.info("Successfully downloaded the JSON metadata file.")
                # Return the file as a response
                return send_file(
                    manifest_json_file,
                    as_attachment=True,
                    download_name=file_name,
                )

            except Exception as ex_download:
                msg = f"An unexpected error occurred for download_edc file for schema_id: {schema_id}: {str(ex_download)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
                ).force_flush()
                response = make_response(jsonify({"error": msg}), 500)
                return response


class MetadataExcelFileDownloadEdc(Resource):
    """
    A Flask-RESTful resource responsible for handling requests for downloading
    metadata Excel files with a specific schema id.

    This class corresponds to the endpoint
    '/metadata_excel_file_download/<int:schema_id>'.
    It handles HTTP requests that include a specific schema id in the URL, and
    it likely implements methods like GET to manage the download_edc of the
    associated metadata Excel file.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating
        new RESTful resources.
    """

    def get(self, schema_id):
        """
        Retrieves the Excel metadata file from Alation based on the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the downloaded Excel metadata file.

        Example:
            Use schema_id 106788TBD to test LAVA_CORE_PROD (DataBricks): lava_core_prod
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alationn
        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
        ).initialize_logging_and_tracing()
        
        azure_trace_exporter = tracer.azure_trace_exporter

        with tracer.start_as_current_span(
            f"metadata_excel_file_download_edc/{schema_id}"
        ):
            try:

                start_time = time.time()  # Record the start time

                config = app.cdc_config

                obj_file = cdc_env_file.EnvironmentFile()
                app_dir = os.path.dirname(os.path.abspath(__file__))
                parent_dir = os.path.dirname(app_dir)

                repository_path = config.get("repository_path")
                environment = config.get("environment")

                schema = alation_schema.Schema()
                excel_data_definition_file = schema.get_excel_data_definition_file_path(
                    repository_path, environment
                )
                manifest_excel_file = schema.download_manifest_excel(
                    schema_id,
                    config,
                    excel_data_definition_file,
                    DATA_PRODUCT_ID
                )

                # Return the file as a download_edc
                file_name = os.path.basename(manifest_excel_file)
                logger.info(f"file_name:{file_name}")

                end_time = time.time()  # Record the start time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    "start_time": start_time,
                    "end_time": end_time,
                    "total_time": total_time,
                    "data": "Success",
                }

                mime_type = "application/vnd.openxmlformats"
                mime_type = mime_type + "-officedocument.spreadsheetml.sheet"

                # Return the file as a response
                return send_file(
                    manifest_excel_file,
                    as_attachment=True,
                    download_name=file_name,
                )

            except Exception as ex:
                msg = f"An unexpected error occurred for download_edc file for schema_id: {schema_id}: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
                ).force_flush()
                response = make_response(jsonify({"error": str(ex)}), 500)
                return response
            finally:
                # Ensure that all telemetry is flushed to Application Insights before the process ends
                azure_trace_exporter.flush()  # Force flush telemetry

class MetadataExcelFileDownloadCodes(Resource):
    """
    A Flask-RESTful resource responsible for handling requests for downloading
    metadata Excel files with a specific schema id.

    This class corresponds to the endpoint
    '/metadata_excel_file_download/<int:schema_id>'.
    It handles HTTP requests that include a specific schema id in the URL, and
    it likely implements methods like GET to manage the download_edc of the
    associated metadata Excel file.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating
        new RESTful resources.
    """

    def get(self, schema_id):
        """
        Retrieves the Excel metadata file from Alation based on the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the downloaded Excel metadata file.

        Example:
            Use schema_id 106788TBD to test LAVA_CORE_PROD (DataBricks): lava_core_prod
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alationn
        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span(
            f"metadata_excel_file_download_codes/{schema_id}"
        ):
            try:
                start_time = time.time()  # Record the start time

                config = app.cdc_config

                obj_file = cdc_env_file.EnvironmentFile()
                app_dir = os.path.dirname(os.path.abspath(__file__))
                parent_dir = os.path.dirname(app_dir)

                repository_path = config.get("repository_path")
                environment = config.get("environment")

                schema = alation_schema.Schema()
                excel_data_definition_file = schema.get_excel_data_definition_file_path(
                    repository_path, environment
                )
                manifest_excel_file = schema.download_manifest_excel_codes(
                    schema_id,
                    config,
                    excel_data_definition_file,
                    DATA_PRODUCT_ID,
                    ENVIRONMENT,
                )

                # Return the file as a download_edc
                file_name = os.path.basename(manifest_excel_file)
                logger.info(f"file_name:{file_name}")

                end_time = time.time()  # Record the start time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    "start_time": start_time,
                    "end_time": end_time,
                    "total_time": total_time,
                    "data": "Success",
                }

                mime_type = "application/vnd.openxmlformats"
                mime_type = mime_type + "-officedocument.spreadsheetml.sheet"

                # Return the file as a response
                return send_file(
                    manifest_excel_file,
                    as_attachment=True,
                    download_name=file_name,
                )

            except Exception as ex:
                msg = f"An unexpected error occurred for download_edc file for schema_id: {schema_id}: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, DATA_PRODUCT_ID, ENVIRONMENT
                ).force_flush()
                response = make_response(jsonify({"error": str(ex)}), 500)
                return response


class AzSubscriptionClientSecretVerification(Resource):
    """
    A Flask-RESTful resource for handling the verification of API keys.

    """

    def get(self):
        """
        Verifies the key stored in key vault based on configuration setting: az_sub_web_client_secret_key

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("verify_az_sub_client_secret"):
            config = app.cdc_config
            az_sub_web_client_secret_key = config.get("az_sub_web_client_secret_key")
            az_sub_web_client_secret_key = az_sub_web_client_secret_key.replace(
                "-", "_"
            )
            client_secret = os.getenv(az_sub_web_client_secret_key)
            tenant_id = config.get("az_sub_tenant_id")
            client_id = config.get("az_sub_client_id")

            security_core = cdh_security_core.SecurityCore()
            (
                status_code,
                response_content,
            ) = security_core.verify_az_sub_client_secret(
                tenant_id, client_id, client_secret, DATA_PRODUCT_ID, ENVIRONMENT
            )

            # Handle the verification logic
            return {
                "status_code": status_code,
                "response_content": response_content,
            }


class ConnectApiKeyVerification(Resource):
    """
    A Flask-RESTful resource for handling the verification of API keys.

    """

    def get(self):
        """
        Verifies the key stored in key vault based on configuration setting: az_kv_posit_connect_secret_key

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"connect_api_key_verification"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            connect_api_key = get_posit_api_key()
            posit_connect = cdh_posit_connect.PositConnect()
            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.verify_api_key(
                connect_api_key, posit_connect_base_url, DATA_PRODUCT_ID, ENVIRONMENT
            )

            # Handle the verification logic
            return {
                "status_code": status_code,
                "posit_connect_base_url": posit_connect_base_url,
                "api_url": api_url,
                "connect_api_key": connect_api_key,
                "response_content": response_content,
            }


class DeploymentBundle(Resource):
    """
    A Flask-RESTful resource for handling POSIT Deployment Bundle.

    """

    def get(self, content_id, bundle_id):
        """
        Generates DeploymentBundle

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("build_deployment_bundle"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key"
            )
            connect_api_key = get_posit_api_key()
            posit_connect = cdh_posit_connect.PositConnect()
            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.build_deployment_bundle(
                connect_api_key,
                posit_connect_base_url,
                content_id,
                bundle_id,
                DATA_PRODUCT_ID,
                ENVIRONMENT,
            )

            # Handle the verification logic
            return {
                "posit_connect_base_url": posit_connect_base_url,
                "api_url": api_url,
                "response_content": response_content,
            }


class PythonInformation(Resource):
    """
    A Flask-RESTful resource for handling POSIT Python Information.

    """

    def get(self):
        """
        Generates python information about POSIT

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"api_key_verification"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key"
            )
            connect_api_key = get_posit_api_key()
            posit_connect = cdh_posit_connect.PositConnect()
            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.get_python_information(
                connect_api_key, posit_connect_base_url
            )

            # Handle the verification logic
            return {
                "posit_connect_base_url": posit_connect_base_url,
                "api_url": api_url,
                "az_kv_posit_connect_secret_key": az_kv_posit_connect_secret_key,
                "response_content": response_content,
            }


class GeneratedManifestJson(Resource):
    """
    A Flask-RESTful resource for handling POSIT ManifestJson Generation

    """

    def get(self):
        """
        Generates manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"generate_manifest"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            # Get the full URL
            full_url = request.url
            # Split the URL by '/'
            url_parts = full_url.split("/")
            # Remove the last 2 parts (i.e., the file name or the route)
            url_parts = url_parts[:-2]
            # Join the parts back together
            url_without_filename = "/".join(url_parts)
            base_url = url_without_filename
            environment = config.get("environment")
            obj_file = cdc_env_file.EnvironmentFile()

            app_dir = os.path.dirname(os.path.abspath(__file__))

            manifest_path = app_dir + "/" + environment + "_posit_manifests/"

            swagger_path = app_dir + "/" + environment + "_swagger_manifests/"

            yyyy = str(datetime.now().year)
            dd = str(datetime.now().day).zfill(2)
            mm = str(datetime.now().month).zfill(2)

            json_extension = "_" + yyyy + "_" + mm + "_" + dd + ".json"
            manifest_json_file = manifest_path + "manifest" + json_extension
            # swagger_file = swagger_path + "swagger" + json_extension
            # use cached json file for now
            # having issues downloading
            swagger_file = swagger_path + "swagger_2023_06_22.json"
            connect_api_key = get_posit_api_key()
            requirements_file = app_dir + "/requirements.txt"

            # headers = {
            #     "Authorization": f"Bearer {connect_api_key}",
            # }
            swagger_url = f"{base_url}/swagger.json"
            # response = requests.get(swagger_url, headers=headers)

            # response_data = None
            # error_message = None
            # if response.status_code == 200:  # HTTP status code 200 means "OK"
            #     try:
            #         response_data =  response.json()
            #         response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
            #   except requests.HTTPError as http_err:
            #        error_message = f"HTTP error occurred: {http_err}"
            #        soup = BeautifulSoup(response.text, 'html.parser')
            #        error_message = (soup.prettify())
            #    except JSONDecodeError:
            #        error_message = "The response could not be decoded as JSON."
            #        soup = BeautifulSoup(response.text, 'html.parser')
            #        error_message = (soup.prettify())
            #    except Exception as err:
            #        error_message = f"An error occurred: {err}"
            #        error_message = "Response content:"+ response.content.decode()
            # else:
            #    error_message = f"Request failed with status code {response.status_code}"
            # if error_message is not None:
            #    return {
            #        'headers' : headers,
            #        'swagger_url' :  swagger_url,
            #        'manifest_json': "",
            #        'status_message': error_message
            #    }, 500
            # with open(swagger_file, 'w') as f:
            #    f.write(response_data)

            logger.info(f"swagger_file:{swagger_file}")

            posit_connect = cdh_posit_connect.PositConnect()

            manifest_json = posit_connect.generate_manifest(
                swagger_file, requirements_file
            )

            with open(manifest_json_file, "w") as f:
                f.write(manifest_json)

            # Handle the verification logic
            return {
                "swagger_url": swagger_url,
                "manifest_json": manifest_json,
                "status_message": "success",
            }


class PublishManifestJson(Resource):
    """
    A Flask-RESTful resource for handling POSIT ManifestJsonJson Publication

    """

    def get(self):
        """
        Publishes manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"publish_manifest"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            # Get the full URL
            full_url = request.url
            # Split the URL by '/'
            url_parts = full_url.split("/")
            # Remove the last 2 parts (i.e., the file name or the route)
            url_parts = url_parts[:-2]
            # Join the parts back together
            url_without_filename = "/".join(url_parts)
            base_url = url_without_filename
            environment = config.get("environment")
            obj_file = cdc_env_file.EnvironmentFile()

            app_dir = os.path.dirname(os.path.abspath(__file__))

            manifest_path = app_dir + "/" + environment + "_posit_manifests/"

            manifest_json_file = obj_file.get_latest_file(manifest_path, "json")

            logger.info(f"manfiest_file:{manifest_json_file}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key"
            )
            connect_api_key = get_posit_api_key()

            posit_connect = cdh_posit_connect.PositConnect()

            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.publish_manifest(
                connect_api_key, posit_connect_base_url, manifest_json_file
            )

            # Handle the verification logic
            return {
                "status_code": status_code,
                "response_content": response_content,
                "api_url": api_url,
            }


class ContentList(Resource):
    """
    A Flask-RESTful resource for handling POSIT Content Lists

    """

    def get(self):
        """
        Retrieves the manifest JSON for the content list.

        Returns:
            tuple: A tuple containing the status code and response from the server.
                   The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("list_content"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            connect_api_key = get_posit_api_key()

            posit_connect = cdh_posit_connect.PositConnect()

            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.list_content(connect_api_key, posit_connect_base_url)

            # Handle the verification logic
            return {
                "status_code": status_code,
                "response_content": response_content,
                "api_url": api_url,
            }


class DeploymentBundleList(Resource):
    """
    A Flask-RESTful resource for handling POSIT Bundle Lists

    """

    def get(self, content_id):
        """
        Publishes manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("list_deployment_bundles"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key"
            )
            connect_api_key = get_posit_api_key()

            posit_connect = cdh_posit_connect.PositConnect()

            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.list_deployment_bundles(
                connect_api_key, posit_connect_base_url, content_id
            )

            # Handle the verification logic
            return {
                "status_code": status_code,
                "response_content": response_content,
                "api_url": api_url,
            }


class TaskStatus(Resource):
    """
    A Flask-RESTful resource for handling POSIT Bundle Lists

    """

    def get(self, task_id):
        """
        Gets Task Status

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"get_task_status"):
            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key"
            )
            connect_api_key = get_posit_api_key()

            posit_connect = cdh_posit_connect.PositConnect()

            (
                status_code,
                response_content,
                api_url,
            ) = posit_connect.get_task_details(
                connect_api_key, posit_connect_base_url, task_id
            )

            # Handle the verification logic
            return {
                "status_code": status_code,
                "response_content": response_content,
                "api_url": api_url,
            }


upload_parser_edc = api.parser()
upload_parser_edc.add_argument(
    "file", location="files", type=FileStorage, required=True
)

job_run_parser = api.parser()
job_run_parser.add_argument(
    "environment", location="form", type=str, required=True
)
job_run_parser.add_argument(
    "data_product_id", location="form", type=str, required=True
)
job_run_parser.add_argument(
    "job_name", location="form", type=str, required=True
)
 
 
upload_codes_form_parser = api.parser()
upload_codes_form_parser.add_argument(
    "file", location="files", type=FileStorage, required=True
)
upload_codes_form_parser.add_argument(
    "data_product_id", location="form", type=str, required=True
)
upload_codes_form_parser.add_argument(
    "environment", location="form", type=str, required=True
)

# Define the API description with a hyperlink to the log file page
api.description = API_DESCRIPTION

ns_welcome.add_resource(WelcomeSwagger, "/")
ns_welcome.add_resource(WelcomeSwagger, "/api/swagger")
ns_jira.add_resource(
    Task,
    "/task/<string:jira_project>/<string:jira_component>/', defaults={'jira_fields': None}",
)
ns_jira.add_resource(
    Issue, "/issue/<string:jira_project>/<string:jira_issue_id>/<string:jira_fields>"
)
ns_jira.add_resource(
    Issue,
    "/issue/<string:jira_project>/<string:jira_issue_id>/",
    defaults={"jira_fields": None},
)

# This model is used for swagger documentation
ns_alation.add_resource(
    MetadataJsonFileDownload, "/metadata_json_file_download/<int:schema_id>"
)

ns_alation.add_resource(
    MetadataExcelFileDownloadEdc, "/metadata_excel_file_download_edc/<int:schema_id>"
)

ns_cdh_configuration.add_resource(
    MetadataExcelFileDownloadCodes,
    "/metadata_excel_file_download_codes/<int:schema_id>",
)

class JobRun(Resource):
    @api.expect(job_run_parser, validate=True)
    # comment out for now TODO Fix
    # @azure_ad_authentication
    def post(self):
   
        with tracer.start_as_current_span("job_run") as span:
            try:
                start_time = time.time()  # Record the start time

                trace_id = span.context.trace_id  # Correct way to access trace_id from the active span
                trace_id_hex = format(trace_id, '032x')  # 32-character hexadecimal string

                # Get the uploaded file
                args = job_run_parser.parse_args()
                data_product_id = args["data_product_id"]
                job_name = args["job_name"]
                environment = args["environment"]

                current_file_path = os.path.abspath(__file__)
                current_directory = os.path.dirname(current_file_path)
                logger.info(f"current_directory: {current_directory}")
                # Set repository_path to the premier_rep directory that is a peer of the current directory
                repository_path = os.path.join(current_directory, "../")

                # Ensure the path is absolute and normalized
                repository_path = os.path.abspath(repository_path)

                logger.info(f"repository_path:{repository_path}")
                authenticated_user_id = request.cookies.get("user_id", "unknown")
                current_dir = os.path.dirname(__file__)

                # Construct the path to the peer directory "lava_core" and the .env file inside it
                dotenv_path = os.path.join(os.path.dirname(current_dir), "lava_core", ".env")
                logger.info(f"dotenv_path:{dotenv_path}")
                # If the .env file in lava_core does not exist, fallback to the .env in the parent directory
                if not os.path.exists(dotenv_path):
                    dotenv_path = os.path.join(os.path.dirname(current_dir), ".env")
                logger.info(f"dotenv_file_path:{dotenv_path}")
                # Load the .env file
                load_dotenv(dotenv_path)
                token = os.getenv("CDH_LAVA_PROD_SPN_PAT")
                host = os.getenv("DATABRICKS_HOST")
                host = host.rstrip("/")

                config = {
                "data_product_id": data_product_id,
                "environment": environment,
                }

                logger.info(f"host: {host}")

                rest_client = RestClient(token, host, config=config)
                jobs_client = JobsClient(rest_client)
                two_digit_month = datetime.now().strftime("%m")
                full_job_name = f"{data_product_id}_{job_name}_{environment}"
                # Arrange
                params = {
                    "existing_cluster_id": "0109-184947-l0ka6b1y",  # Replace with your actual cluster ID
                    "name": full_job_name,  # Job name
                    "notebook_task": {
                        "notebook_path": f"/Repos/CDH_LAVA/cdh-lava-core-main/{data_product_id}/_run_jobs_{data_product_id}",  # Path to your Python notebook in Databricks
                        "base_parameters": {
                            "job_name": job_name,  # Add the job_name parameter
                            "report_dd": "NA",  # Add the report_dd parameter
                            "report_mm": two_digit_month,  # Add the report_mm parameter
                            "report_yyyy": "2024",  # Add the report_yyyy parameter
                        },
                    },
                }

                # Act
                result = jobs_client.create(params, run_now=True)

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time
                total_time_string = format_time(total_time)

                # Create the return message with the start, end, and total time
                message = {
                    "trace_id": trace_id_hex,
                    "total_time": total_time_string,
                    "data": "Success"
                }

                 
                response = make_response(jsonify(message), 200)
                # Set up custom CORS headers

                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {"data": msg}

                response = make_response(jsonify(message), 500)
                return response




 
class MetadataExcelFileUploadCodes(Resource):
    """
    A Flask-RESTful resource for handling the upload_Codes of metadata Excel files.

    This class corresponds to the endpoint '/metadata_excel_file_upload'.
    It handles HTTP requests for uploading metadata Excel files.
    Each method in this class corresponds to a specific HTTP
    method (e.g., POST) and carries out the upload operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.

    Returns:
        Response: The response of the HTTP request after processing the
        uploaded file. The specific content and status code of the response
        will depend on the implementation.
    """


    
    @api.expect(upload_codes_form_parser, validate=True)
    # comment out for now TODO Fix
    @azure_ad_authentication
    def post(self):
        """
        Uploads the Excel metadata file to Alation via direct upload_Codes based on
        the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the response data.

        Example:
            Use schema_id 106788 to test LAVA_CORE_PROD (DataBricks): lava_core_prod
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alation
        """

        with tracer.start_as_current_span("metadata_excel_file_upload_codes") as span:
            try:
                start_time = time.time()  # Record the start time

                trace_id = span.context.trace_id  # Correct way to access trace_id from the active span
                trace_id_hex = format(trace_id, '032x')  # 32-character hexadecimal string

                # Get the uploaded file
                
                args = upload_codes_form_parser.parse_args()
                file = args["file"]
                # Read the contents of the file as JSON
                file_contents = file.read()
                data_product_id = args["data_product_id"]
                obj_excel_config_uploader = ExcelConfigUploader()
                repository_path = config.get("repository_path")

                current_file_path = os.path.abspath(__file__)
                current_directory = os.path.dirname(current_file_path)
                logger.info(f"current_directory: {current_directory}")
                # Set repository_path to the premier_rep directory that is a peer of the current directory
                repository_path = os.path.join(current_directory, "../")

                # Ensure the path is absolute and normalized
                repository_path = os.path.abspath(repository_path)

                logger.info(f"repository_path:{repository_path}")
                environment = config.get("environment")
                authenticated_user_id = request.cookies.get("user_id", "unknown")

                manifest_excel_file_path_temp = (
                    obj_excel_config_uploader.get_excel_config_file_path(
                        repository_path,
                        data_product_id,
                        environment,
                        authenticated_user_id,
                    )
                )

                # Get the directory path without the file name
                directory_path = os.path.dirname(manifest_excel_file_path_temp)
                directory_path = directory_path.replace(
                    "/home/nfs/cdc/", "/home/nfs/CDC/"
                )

                # Log the action of creating directories
                logger.info(f"Ensure directory exists: {directory_path}")

                manifest_excel_file_path_temp = manifest_excel_file_path_temp.replace(
                    "/home/nfs/cdc/", "/home/nfs/CDC/"
                )

                # Create the directory if it does not exist
                os.makedirs(directory_path, exist_ok=True)

                with open(manifest_excel_file_path_temp, "ab") as f:
                    # Log the file open action
                    logger.info(
                        f"File opened successfully: {manifest_excel_file_path_temp}"
                    )

                directory_path = os.path.dirname(manifest_excel_file_path_temp)

                # Log the action of creating directories
                logger.info(f"Ensure directory exists: {directory_path}")

                # Create the directory if it does not exist
                os.makedirs(directory_path, exist_ok=True)

                with open(manifest_excel_file_path_temp, "ab") as f:
                    # Log the file open action
                    logger.info(
                        f"File opened successfully: {manifest_excel_file_path_temp}"
                    )
                    f.write(file_contents)

                 
                obj_excel_sheet_combiner = ExcelSheetCombiner()
             
                
                result_df = obj_excel_sheet_combiner.combine_sheets(manifest_excel_file_path_temp, data_product_id, environment)
                base_path = os.path.dirname(manifest_excel_file_path_temp)
                source_path = os.path.join(base_path, data_product_id + '_code_local_valuesets.csv')

                # Add debug logging for the source_path
                logger.info(f"Attempting to save to source_path: {source_path}")

                # Check if the directory exists
                directory = os.path.dirname(source_path)
                if not os.path.exists(directory):
                    logger.error(f"Directory does not exist: {directory}")
                    raise OSError(f"Cannot save file to a non-existent directory: {directory}")

                # Try writing to CSV and catch any errors
                try:
                    logger.info(f"Resulting DataFrame: {result_df.head()}")  # Log first few rows of the DataFrame
                    result_df.to_csv(source_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
                    logger.info(f"File successfully saved to: {source_path}")
                except Exception as e:
                    logger.error(f"Failed to save CSV to {source_path}: {str(e)}")
                
                destination_path = f"https://edavcdhproddlmprd.dfs.core.windows.net/cdh/raw/lava/{data_product_id}/data/local/{data_product_id}_code_local_valuesets.csv"
                from_to = "LocalBlobFS"

                # Call the method
                obj_storage_file = AzStorageFile()
                dbutils=None
                result = obj_storage_file.file_adls_copy(
                config, source_path, destination_path, from_to, dbutils, data_product_id, environment
                )

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time
                total_time_string = format_time(total_time)

                # Create the return message with the start, end, and total time
                message = {
                    "trace_id": trace_id_hex,
                    "total_time": total_time_string,
                    "data": "Success",
                    "file_path" : manifest_excel_file_path_temp
                }

                 
                response = make_response(jsonify(message), 200)
                # Set up custom CORS headers

                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {"data": msg}

                response = make_response(jsonify(message), 500)
                return response


class MetadataExcelFileUploadEdc(Resource):
    """
    A Flask-RESTful resource for handling the upload_edc of metadata Excel files.

    This class corresponds to the endpoint '/metadata_excel_file_upload'.
    It handles HTTP requests for uploading metadata Excel files.
    Each method in this class corresponds to a specific HTTP
    method (e.g., POST) and carries out the upload operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.

    Returns:
        Response: The response of the HTTP request after processing the
        uploaded file. The specific content and status code of the response
        will depend on the implementation.
    """

    @api.expect(upload_parser_edc, validate=True)
    @azure_ad_authentication
    def post(self):
        """
        Uploads the Excel metadata file to Alation via direct upload_edc based on
        the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the response data.

        Example:
            Use schema_id 106788 to test LAVA_CORE_PROD (DataBricks): lava_core_prod
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alation
        """

        with tracer.start_as_current_span("metadata_excel_file_upload_edc"):
            try:
                start_time = time.time()  # Record the start time

                # Get the uploaded file
                args = upload_parser_edc.parse_args()
                file = args["file"]
                # Read the contents of the file as JSON
                file_contents = file.read()

                schema = alation_schema.Schema()
                repository_path = config.get("repository_path")
                environment = config.get("environment")
                alation_user_id = 7

                manifest_excel_file_path_temp = (
                    schema.get_excel_manifest_file_path_temp(
                        "upload_edc", repository_path, environment, alation_user_id
                    )
                )

                with open(manifest_excel_file_path_temp, "wb") as f:
                    f.write(file_contents)

                schema_json_file_path = schema.get_json_data_definition_file_path(
                    repository_path, environment
                )

                authenticated_user_id = request.cookies.get("user_id")

                (
                    content_result,
                    authorized_tables_count,
                    unauthorized_table_count,
                ) = schema.upload_edc_manifest_excel(
                    manifest_excel_file_path_temp,
                    config,
                    schema_json_file_path,
                    authenticated_user_id,
                )

                logger.info(f"content_result: {content_result}")

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time
                total_time_string = format_time(total_time)

                # Create the return message with the start, end, and total time
                message = {
                    "total_time": total_time_string,
                    "authorized_tables_count": authorized_tables_count,
                    "unauthorized_table_count": unauthorized_table_count,
                    "data": "Success",
                }

                response = make_response(jsonify(message), 200)
                # Set up custom CORS headers

                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {"data": msg}

                response = make_response(jsonify(message), 500)
                return response


class MetadataJsonFileUploadEdc(Resource):
    """
    A Flask-RESTful resource for handling the upload_edc of metadata JSON files.

    This class corresponds to the endpoint '/metadata_json_file_upload_edc'. It
    handles HTTP requests for upload_edcing metadata JSON files.
    Each method in this class corresponds to a specific HTTP
    method (e.g., POST) and carries out the upload operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.

    Returns:
        Response: The response of the HTTP request after processing the
        uploaded file.
        The specific content and status code of the response will depend on
        the implementation.
    """

    @api.expect(upload_parser_edc, validate=True)
    @azure_ad_authentication
    def post(self):
        """Uploads JSON metadata file via direct upload to Alation
        based on schema_id.
        Use 106788 to test LAVA_CORE_PROD (DataBricks)
        """

        with tracer.start_as_current_span("metadata_json_file_upload_edc"):
            try:
                start_time = time.time()  # Record the start time

                # Get the uploaded file
                args = upload_parser_edc.parse_args()
                file = args["file"]
                # Read the contents of the file as JSON
                file_contents = file.read()
                metadata_json_data = json.loads(file_contents)

                schema = alation_schema.Schema()
                config = app.cdc_config

                repository_path = config.get("repository_path")
                environment = config.get("environment")
                json_data_definition_file_path = (
                    schema.get_json_data_definition_file_path(
                        repository_path, environment, DATA_PRODUCT_ID
                    )
                )

                authenticated_user_id = request.cookies.get("user_id")

                (
                    content_result,
                    authorized_tables_count,
                    unauthorized_table_count,
                ) = schema.upload_manifest_json(
                    metadata_json_data, config, authenticated_user_id
                )

                logger.info(f"content_result: {content_result}")

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    "total_time": total_time,
                    "authorized_tables_count": authorized_tables_count,
                    "unauthorized_table_count": unauthorized_table_count,
                    "data": "Success",
                }

                response = make_response(jsonify(message), 200)
                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {
                    "start_time": start_time,
                    "end_time": end_time,
                    "total_time": total_time,
                    "data": msg,
                }

                response = make_response(jsonify(message), 500)
                return response


ns_alation.add_resource(MetadataJsonFileUploadEdc, "/metadata_json_file_upload_edc")
ns_alation.add_resource(MetadataExcelFileUploadEdc, "/metadata_excel_file_upload_edc")

ns_posit.add_resource(ConnectApiKeyVerification, "/connect_api_key_verification")
ns_posit.add_resource(PythonInformation, "/python_information")
ns_posit.add_resource(GeneratedManifestJson, "/generate_manifest")
ns_posit.add_resource(PublishManifestJson, "/publish_manifest")
ns_posit.add_resource(ContentList, "/list_content")
ns_posit.add_resource(
    DeploymentBundle,
    "/build_deployment_bundle/<string:content_id>/<string:bundle_id>",
)
ns_posit.add_resource(
    DeploymentBundleList, "/list_deployment_bundles/<string:content_id>"
)
ns_posit.add_resource(TaskStatus, "/get_task_status/<string:task_id>")

ns_cdh_security.add_resource(
    AzSubscriptionClientSecretVerification, "/verify_az_sub_client_secret"
)
ns_cdh_security.add_resource(AuthCallback, "/callback")
ns_cdh_security.add_resource(AuthCallback, "/get_user_id")


ns_altmetric.add_resource(
    AltmetricDownload,
    "/download_altmetric_data/<string:altmetric_id>",
    endpoint="altmetric_download",
)

 

ns_cdh_configuration.add_resource(
    MetadataExcelFileUploadCodes, "/metadata_excel_file_upload_codes"
)

ns_cdh_observability.add_resource(DependencyGraph, "/dependency_graph/<string:operation_id>/<string:data_product_id>/<string:environment>/<int:page>")

ns_cdh_orchestration.add_resource(
    JobRun, "/job_run"
)


if __name__ == "__main__":
    app.run(debug=True)