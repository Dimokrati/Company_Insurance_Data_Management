import logging
from util.config_handler import ConfigHandler
from util.db_handler import DbHandler

LOGGER = logging.getLogger(__name__)


class ApiTransformPipeline:
    """class responsible of running the api transform pipeline"""
    def __init__(self):
        self.config_handler = ConfigHandler()
        self.db_handler = DbHandler("insurance_company")

    def run_pipeline(self):
        """function runs the pipeline"""
        LOGGER.info("Starting the api transform pipeline")
        curated_prefixes = self.config_handler.get_prefixes("curated_tables_prefixes")
        self.db_handler.insert_unique_data(curated_prefixes)