from util.api_handler import ApiHandler
import logging

logging.basicConfig(level = logging.INFO)
LOGGER = logging.getLogger(__name__)

class ApiPipeline:
    def __init__(self):
        self.api_handler = ApiHandler()

    def run_pipeline(self):
        LOGGER.info("calling the api")
        return self.api_handler.fetch_data() # calling the fetch_data method to get the data
        # TODO: add function to store data in raw database 