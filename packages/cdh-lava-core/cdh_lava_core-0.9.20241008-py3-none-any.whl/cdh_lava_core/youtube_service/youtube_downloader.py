
from pytube import YouTube
from cdh_lava_core.cdc_log_service.environment_logging import LoggerSingleton
import os
import sys
import subprocess

# Get the currently running file name
NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
# Get the parent folder name of the running file
SERVICE_NAME = os.path.basename(__file__)

class YouTubeDownloader:
    """
    A class for downloading YouTube videos.
    """

    @staticmethod
    def download_youtube(link, data_product_id, environment):
        """
        Downloads a YouTube video using the provided link.

        Args:
            link (str): The YouTube video link.
            data_product_id (str): The ID of the data product.
            environment (str): The environment in which the download is performed.

        Raises:
            subprocess.CalledProcessError: If an error occurs during the download process.

        Returns:
            None
        """
        tracer, logger = LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
        ).initialize_logging_and_tracing()

        with tracer.start_as_current_span("download_youtube"):
            try:
                youtube_object = YouTube(link)
                youtube_object = youtube_object.streams.get_highest_resolution()
                youtube_object.download_youtube()
                print("Youtube download is completed successfully.")
            except subprocess.CalledProcessError as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                LoggerSingleton.instance(
                    NAMESPACE_NAME, SERVICE_NAME, data_product_id, environment
                ).error_with_exception(error_msg, exc_info)
                raise


if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    YouTubeDownloader.download(link)
