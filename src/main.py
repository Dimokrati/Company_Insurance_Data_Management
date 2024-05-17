from pipelines.raw.api_pipeline import ApiPipeline
import logging

logging.basicConfig(level = logging.INFO)
LOGGER = logging.getLogger(__name__)

api_pipeline = ApiPipeline("API-1")


def main():
    LOGGER.info("Starting the management process")
    api_pipeline.run_pipeline()
    


if __name__ == "__main__":
    main()
