import logging
from util.config_handler import ConfigHandler
from util.db_handler import DbHandler

LOGGER = logging.getLogger(__name__)



class LoadPipeline:
    def __init__(self):
        self.config_handler = ConfigHandler()
        self.db_handler = DbHandler("insurance_company")

    def run_load_pipeline(self):
        """powring the data warehouse"""
        LOGGER.info("Starting the dw powring pipeline")
        self.db_handler.powering_dims_dw()
        self.db_handler.powering_fact_dw()