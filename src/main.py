from pipelines.raw.api_pipeline import ApiPipeline
from pipelines.curated.api_transfrom_pipeline import ApiTransformPipeline
from pipelines.dw.api_dw_pipeline import ApiDwPipeline
import logging

logging.basicConfig(level = logging.INFO, format="[%(asctime)s]   %(levelname)s: '%(message)s' - SOURCE:%(module)s")
LOGGER = logging.getLogger(__name__)

api_pipeline = ApiPipeline("API-1")
api_transform_pipeline = ApiTransformPipeline()
api_dw_pipeline = ApiDwPipeline()


def main():
    LOGGER.info("Starting the management process")
    api_pipeline.run_pipeline()
    api_transform_pipeline.run_pipeline()
    api_dw_pipeline.run_pipeline()
    
    


if __name__ == "__main__":
    main()
