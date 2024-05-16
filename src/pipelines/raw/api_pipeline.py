from util.api_handler import ApiHandler
import logging

LOGGER = logging.getLogger(__name__)

class ApiPipeline:
    def __init__(self, api_name):
        self.api_name = api_name
        self.api_handler = ApiHandler(self.api_name)

    def run_pipeline(self):
        LOGGER.info("calling the api")
        return self.api_handler.fetch_data() # calling the fetch_data method to get the data
        # TODO: add function to store data in raw database 