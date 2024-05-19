from util.api_handler import ApiHandler
from util.db_handler import DbHandler
from util.config_handler import ConfigHandler
import logging


LOGGER = logging.getLogger(__name__)

class ApiPipeline:
    def __init__(self, api_name):
        self.api_name = api_name
        self.config_handler = ConfigHandler()
        self.api_handler = ApiHandler(self.api_name)
        self.db_handler = DbHandler("insurance_company")

    def run_pipeline(self):
        LOGGER.info("Starting the api pipeline")
        data = self.api_handler.fetch_data() # calling the fetch_data method to get the data
        # raw_prefixes = self.config_handler.get_prefixes("raw_tables_prefixes")
        self.db_handler.insert_data(data, "raw_data", "raw")