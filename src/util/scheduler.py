import schedule
import time
from pipelines.raw.api_pipeline import ExtractPipeline
from pipelines.curated.api_transfrom_pipeline import TransformPipeline
from pipelines.dw.api_dw_pipeline import LoadPipeline

class Scheduler:
    def __init__(self):
        self.extract_pipeline = ExtractPipeline("API-1")
        self.transform_pipeline = TransformPipeline()
        self.load_pipeline = LoadPipeline()

    def main_pipeline(self):
        self.extract_pipeline.run_extract_pipeline()
        self.transform_pipeline.run_transform_pipeline()
        self.load_pipeline.run_load_pipeline()

    def schedule_jobs(self):
        schedule.every().day.at("12:00").do(self.main_pipeline)
        schedule.every().day.at("19:00").do(self.main_pipeline)
        schedule.every().sunday.do(lambda: None)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def trigger_main_pipeline(self):
        self.main_pipeline()
