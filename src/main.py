import logging
import argparse
from util.scheduler import Scheduler

logging.basicConfig(level = logging.INFO, format="[%(asctime)s]   %(levelname)s: '%(message)s' - SOURCE:%(module)s")
LOGGER = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Management process of insurance data")
    parser.add_argument("-m", "--manual", action="store_true", help="Trigger the pipeline manually")
    args = parser.parse_args()

    LOGGER.info("Starting the management process of insurance data")
    scheduler = Scheduler()

    if args.manual:
        LOGGER.info("Manually triggering the pipeline...")
        scheduler.trigger_main_pipeline()
    else:
        LOGGER.info("Scheduling jobs...")
        scheduler.schedule_jobs()
    
    
if __name__ == "__main__":
    main()
