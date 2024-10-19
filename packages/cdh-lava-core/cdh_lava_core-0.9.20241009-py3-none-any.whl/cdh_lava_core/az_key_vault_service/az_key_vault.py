from azure.identity import ClientSecretCredential, DeviceCodeCredential, InteractiveBrowserCredential
from azure.keyvault.secrets import SecretClient
import os
import sys

from cdh_lava_core.cdc_log_service.environment_logging import LoggerSingleton
import sys

# Get the currently running file name
NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
# Get the parent folder name of the running file
SERVICE_NAME = os.path.basename(__file__)


class AzKeyVault:
    """Wrapper class for Azure Key Vault to get secrets.

    This class authenticates with the Azure Key Vault using a service
    principal and provides a method to retrieve secrets.
    """

    # Get the currently running file name
    NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
    # Get the parent folder name of the running file
    SERVICE_NAME = os.path.basename(__file__)

    def __init__(
        self,
        tenant_id,
        client_id,
        client_secret,
        key_vault_name,
        running_interactive,
        data_product_id,
        environment,
        client_secret_key=None,
    ):
        """
        Initializes an instance of the AzKeyVault class.

        Args:
            tenant_id (str): The Azure Active Directory tenant ID.
            client_id (str): The client ID of the Azure AD application.
            client_secret (str): The client secret of the Azure AD application.
            key_vault_name (str): The name of the Azure Key Vault.
            running_interactive (bool): Indicates whether the code is running in an interactive environment.
            data_product_id (str): The ID of the data product.
            environment (str): The environment in which the code is running.
            client_secret_key (str, optional): The client spn secret key. Defaults to None.

        Returns:
            None
        """

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("__init__"):
            try:
                self.vault_url = f"https://{key_vault_name}.vault.azure.net/"
                self.running_interactive = running_interactive
                self.client_id = client_id
                self.client_secret = client_secret
                self.tenant_id = tenant_id
                self.data_product_id = data_product_id
                self.environment = environment

                if running_interactive is True:
                    self.credential_device = self.get_credential_device()
                    self.client_device = self.get_secret_client(self.credential_device)

                    if client_secret is not None and client_secret != "":
                        self.credential = self.get_credential()
                        self.client_spn = self.get_secret_client(self.credential)
                        self.client = self.client_spn
                    else:
                        self.client = self.client_device

                    if client_secret_key is None:
                        error_msg = f"client_secret_key is None: Unable to retrieve secret from key vault"
                        raise ValueError(error_msg)
                    client_secret = self.get_secret(client_secret_key)
                    self.client_secret = client_secret
                else:
                    # Non Interactive
                    if client_secret_key is None:
                        error_msg = "client_secret_key is None: Unable to retrieve secret from key vault"
                        raise ValueError(error_msg)
                    if client_secret is not None and client_secret != "":
                        self.credential = self.get_credential()
                        self.client_spn = self.get_secret_client(self.credential)
                        self.client = self.client_spn
                    else:
                        logger.info(f"fetching secret for key: {client_secret_key}")
                        self.client_secret = self.get_secret(client_secret_key)
                        if self.client_secret is None:
                            raise ValueError(f"Failed to get secret for key: {self.client_secret}")
                        logger.info(f"client_secret for key:{client_secret_key} has length: {len(str(self.client_secret) )}")
                        self.credential = self.get_credential()
                        self.client_spn = self.get_secret_client(self.credential)
                        self.client = self.client_spn

                logger.info(f"vault_url:{self.vault_url}")
                logger.info(f"tenant_id:{self.tenant_id}")
                logger.info(f"client_id:{self.client_id}")
                logger.info(f"client_secret_length:{len(str(self.client_secret))}")
                logger.info(f"running_interactive:{str(self.running_interactive)}")


                if not self.client_secret:
                    raise ValueError("Client secret is missing or invalid.")
                    
                # self.credential_default = DefaultAzureCredential()
                # self.credential_dev =  AzureDeveloperCliCredential(  tenant_id=tenant_id,additionally_allowed_tenants=['*'])
                # self.client_default = SecretClient(vault_url,credential= self.credential_default)
                # self.client_dev = SecretClient(vault_url, credential=self.credential_dev)

                # Create a KeyVaultTokenCallback object
                # callback_dev = azure.keyvault.secrets.KeyVaultTokenCallback(self.credential_dev)
                # Set the KeyVaultTokenCallback object on the SecretClient object
                # self.client_dev.authentication_callback = self.callback_dev

            except Exception as ex:
                error_msg = "Error: %s %s", client_secret_key, ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise

    def get_access_token(self):
        """
        Retrieves an access token using the Azure Active Directory client secret credential.

        The function uses a client secret credential, which consists of the tenant ID, client ID,
        and client secret, to authenticate with Azure Active Directory and obtain an access token.
        The access token can then be used to authenticate requests to Azure services.

        The configuration settings and client secret are retrieved from the environment variables.

        Returns:
        str: The access token.

        Raises:
        azure.core.exceptions.ClientAuthenticationError: If there's a problem with
            client authentication, such as an invalid client secret.

        Note:
        Ensure that the required environment variables are set and the necessary permissions
        are granted in Azure AD for the app registration. The client secret should be stored securely,
        and it's recommended to use a secure method to retrieve it (such as Azure Key Vault).

        Common default Azure Scopes are:

        Azure Management API:
            - value: "https://management.azure.com/.default"
            - description: Used for managing and accessing Azure resources through the Azure Resource Manager.
        Microsoft Graph API:
            - value: "https://graph.microsoft.com/.default"
            - description: Used for accessing resources in the Microsoft Graph, such as user profiles, mail, calendar, and more. It's a unified API endpoint for accessing data across Microsoft 365 services.
        Azure Storage:
            - value: "https://storage.azure.com/.default"
            - description: "Used for accessing Azure Storage services, including Blob, File, Queue, and Table storage."
        Azure Key Vault:
            - value: "https://vault.azure.net/.default"
            - description: "Used for accessing secrets, keys, and certificates stored in Azure Key Vault."
        Azure SQL Database:
            - value: "https://database.windows.net/.default"
            - description: "Used for accessing Azure SQL Database resources."
        Azure Service Bus:
            - value: "https://servicebus.azure.net/.default"
            - description: "Used for accessing Azure Service Bus resources, such as queues and topics."
        Azure Event Hubs:
            - value: "https://eventhubs.azure.net/.default"
            - description: "Used for accessing Azure Event Hubs resources."
        Azure Active Directory Scopes
            - value: "https://graph.windows.net/.default"
            - description: "Used for accessing Azure Active Directory resources through the older Azure AD Graph API.
        """

        data_product_id = self.data_product_id
        environment = self.environment

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("get_access_token"):
            try:
                # Get the access token
                # SPN only currently has access to https://graph.windows.net/.default

                credential = self.get_credential()
                token = credential.get_token(
                    "https://management.azure.com/.default"
                )

                # token = self.credential.get_token(
                #    "https://management.azure.com/.default"
                # )
                logger.info(f"token_length:{len(token.token)}")
                return token.token

            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise

    def cdc_authentication_callback(self, client, context):
        """
        Callback function for CDC authentication.

        This function obtains an access token from a custom authentication mechanism.

        Args:
            cls: The class object.
            client: The client object.
            context: The authentication context.

        Returns:
            The access token.

        """

        data_product_id = self.data_product_id
        environment = self.environment

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("cdc_authentication_callback"):
            try:
                access_token = self.get_access_token()

                logger.info(f"access_token_length:{len(access_token)}")
                # Return the access token
                return access_token

            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise

    def get_credential_device(self):
        """Gets the DeviceCodeCredential for interactive running mode.

        Returns:
            DeviceCodeCredential: The DeviceCodeCredential object for authentication.
        """

        data_product_id = self.data_product_id
        environment = self.environment

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("get_credential_device"):
            return DeviceCodeCredential(
                client_id=self.client_id,
                tenant_id=self.tenant_id,
                additionally_allowed_tenants=["*"],
            )

    def get_credential(self):
        """Gets the ClientSecretCredential for non-interactive running mode.

        Returns:
            ClientSecretCredential: The ClientSecretCredential object for authentication.

        Raises:
            Exception: If an error occurs while retrieving the credential.
        """

        data_product_id = self.data_product_id
        environment = self.environment
        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("get_credential"):
            try:
                client_id = self.client_id
                tenant_id = self.tenant_id
                logger.info(f"get_credential client_id: {client_id}")
                logger.info(f"get_credential tenant_id: {tenant_id}")
                logger.info(
                    f"get_credential client_secret_length: {len(str(self.client_secret))}"
                )

                return ClientSecretCredential(
                    client_id=self.client_id,
                    tenant_id=self.tenant_id,
                    client_secret=self.client_secret,
                )

            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise

    def get_secret_client(self, credential):
        """
        Creates a SecretClient using a given credential.

        Args:
            credential: The credential used to authenticate with the Azure Key Vault.

        Returns:
            A SecretClient instance.

        """

        data_product_id = self.data_product_id
        environment = self.environment

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("get_secret_client"):
            try:
                secret_client = SecretClient(
                    vault_url=self.vault_url, credential=credential
                )
                logger.info("retrieved secret client ")
                return secret_client
            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise

    def retrieve_secret(self, secret_client, secret_name):
        """
        Attempts to retrieve a secret from the Azure Key Vault using a given SecretClient.

        Args:
            secret_client (SecretClient): The SecretClient object used to interact with the Azure Key Vault.
            secret_name (str): The name of the secret to retrieve.

        Returns:
            str: The value of the retrieved secret, or None if the retrieval fails.
        """

        data_product_id = self.data_product_id
        environment = self.environment

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("retrieve_secret"):
            logger.info(f"secret_name: {secret_name}")
            return secret_client.get_secret(secret_name).value

    def get_secret(self, secret_name, secret_scope=None, dbutils=None):
        """
        Retrieves a secret from the Azure Key Vault.

        Args:
            secret_name (str): The name of the secret to retrieve.
            secret_scope (str, optional): The scope of the secret. Defaults to None.

        Returns:
            str: The value of the retrieved secret.

        Raises:
            ValueError: If the secret retrieval fails.
        """

        data_product_id = self.data_product_id
        environment = self.environment
        secret_name = str(secret_name)

        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        span_name = f"get_secret:{secret_name}:from:{self.vault_url}"

        with tracer.start_as_current_span("get_secret"):
            try:
                logger.info(f"span_name:{span_name}")
                logger.info(f"vault_url:{self.vault_url}")
                logger.info(f"tenant_id:{self.tenant_id}")
                logger.info(f"client_id:{self.client_id}")
                logger.info(f"secret_name:{secret_name}")

                env_secret_name = secret_name.replace("-", "_").upper()
                logger.info(
                    f"Pre-check secret from environment variable for key: {env_secret_name}"
                )

                # First try to retrieve the secret from an environment variable
                secret_value = os.environ.get(env_secret_name)

                if secret_value is not None:
                    logger.info(
                        f"Pre-check Retrieved secret from environment variable for key: {env_secret_name}"
                    )
                    return secret_value
                else:
                    logger.info(
                        f"Pre-check Failed to retrieve secret from environment variable for key: {env_secret_name}"
                    )

                try:

                    running_local = not (("dbutils" in locals() or "dbutils" in globals()) and dbutils is not None)
                             
                    if running_local:
                        # try interactive if local
                        credential =  InteractiveBrowserCredential(tenant_id=self.tenant_id, additionally_allowed_tenants=self.tenant_id)
                        kv_uri = self.vault_url
                        default_client = SecretClient(vault_url=kv_uri, credential=credential)
                        
                        secret_value = default_client.get_secret(secret_name)
                        if secret_value is None:
                            logger.info(
                                f"first attempt to retrieve secret for key: {secret_name} from device client"
                            )
                            secret_client = self.client_device
                        else:
                            logger.info(
                                f"first attempt to retrieve secret for key: {secret_name} from spn client"
                            )
                            secret_client = self.client

                        secret_value = self.retrieve_secret(secret_client, secret_name)
                except Exception as ex:
                    logger.warning(
                        f"Failed in first attempt to retrieve secret for key: {secret_name}. Error: {ex}"
                    )
                    secret_value = None

                if secret_value is None and running_local is True:
                    if self.running_interactive is True:
                        # If running in interactive mode
                        # try to retrieve the secret using DeviceCodeCredential
                        logger.info(
                            f"second attempt interactive to retrieve secret for key: {secret_name}"
                        )
                        logger.info(
                            f"running_interactive is True:{str(self.running_interactive)}"
                        )

                        secret_value = self.retrieve_secret(
                            self.client_device, secret_name
                        )

                        if secret_value is not None:
                            logger.info(
                                f"Retrieved secret using DeviceCodeCredential for key: {secret_name}"
                            )
                            return "Secret retrieved using DeviceCodeCredential"
                        else:
                            s_error_msg = (
                                f"Unable to fetch secret from key vault: {secret_name}"
                            )
                            logger.warning(
                                "Failed to retrieve secret using DeviceCodeCredential, falling back to ClientSecretCredential."
                            )
                            secret_value = self.retrieve_secret(
                                self.client, secret_name
                            )
                            raise ValueError(s_error_msg)
                elif secret_value is None and running_local is False:
                    logger.info(
                        f"second attempt non-interactive to retrieve secret for key: {secret_name}"
                    )

                    if dbutils is not None:
                        logger.info("Using dbutils to retrieve secret")
                        # Retrieve secret from dbutils
                        secret_value = dbutils.secrets.get(
                            scope=secret_scope, key=secret_name
                        )
                        logger.info(
                            f"Retrieved secret from dbutils for key: {secret_name}"
                        )

                        if secret_value is not None:
                            return secret_value

                        else:
                            ex_message = (
                                f"Unable to fetch secret from dbutils: {str(ex)}"
                            )
                            error_msg = "Error: %s", secret_name + ":" + ex_message
                            exc_info = sys.exc_info()
                            LoggerSingleton.instance(
                                NAMESPACE_NAME,
                                SERVICE_NAME,
                                data_product_id,
                                environment,
                            ).error_with_exception(error_msg, exc_info)
                            raise ex
                    else:
                        error_msg = "dbutils is None: unable to retrieve secret from dbutils"
                        raise ValueError(error_msg)
                else:
                    logger.info(
                        f"Retrieved secret successfully on first attempt for key: {secret_name}"
                    )
                    return secret_value

            except Exception as ex:
                error_msg = "Error: %s", secret_name + ":" + str(ex)
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise
