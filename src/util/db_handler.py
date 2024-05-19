import pandas as pd
import logging
from datetime import datetime
from sqlalchemy import create_engine, text
from util.config_handler import ConfigHandler

LOGGER = logging.getLogger(__name__)

class DbHandler:
    def __init__(self, db_name):
        self.config_handler = ConfigHandler()
        self.db_name = db_name
        self.params = self.config_handler.get_db_params(db_name)
        self.db_user = self.params['db_user']
        self.db_password = self.params['db_password']
        self.db_host = self.params['db_host']
        self.db_port = self.params['db_port']
        self.db_name = self.params['db_name']
        self.connection_str = f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
        self.engine = create_engine(self.connection_str)

    def split_dataframe_by_prefix(self, df, prefixes):
        """Split the DataFrame into smaller DataFrames based on prefixes."""
        split_dfs = {}
        for prefix in prefixes:
            columns = [col for col in df.columns if col.startswith(prefix + '_')]
            split_dfs[prefix] = df[columns].copy()
            split_dfs[prefix].columns = [col[len(prefix)+1:] for col in columns]  # Remove prefix from column names
        return split_dfs
    
    def create_date_data(self):
        today = datetime.now().date()
        
        day = today.day
        month = today.month
        year = today.year
        day_of_week = today.weekday()  # Monday is 0 and Sunday is 6
        day_of_month = today.day
        day_of_year = today.timetuple().tm_yday
        week_of_year = today.isocalendar()[1]
        quarter = (today.month - 1) // 3 + 1

        # Create a list of dictionaries with the same values for all 7 rows
        data = [{
            'dates_date': today,
            'dates_day': day,
            'dates_month': month,
            'dates_year': year,
            'dates_day_of_weak': day_of_week,
            'dates_day_of_month': day_of_month,
            'dates_day_of_year': day_of_year,
            'dates_week_of_year': week_of_year,
            'dates_quarter': quarter
        } for _ in range(7)]
        
        df = pd.DataFrame(data)
        return df
    
    def insert_data(self, df, table_name, schema_name):
        """Insert the split DataFrames into their respective tables."""
        # split_dfs = self.split_dataframe_by_prefix(df, prefixes.keys())
        date_data = self.create_date_data()
        # date_data.to_sql("raw_dates", self.engine, schema = schema_name, if_exists='append', index=False)
        # LOGGER.info("Inserted data into table raw_dates")
        # for prefix, table_name in prefixes.items():
            # split_dfs[prefix].to_sql(table_name, self.engine, schema = schema_name, if_exists='append', index=False)
        res_df = pd.concat([df,date_data], axis=1)
        res_df.to_sql(table_name, self.engine, schema=schema_name, if_exists='append', index=False)
        LOGGER.info(f"Inserted data into table raw_data")
        


    def extract_data(self,engine):
        query = self.config_handler.get_raw_data_query("query_raw_data")
        df = pd.read_sql(query, engine)
        return df
    
    def remove_duplicates(self,df):
        return df.drop_duplicates()
    

    def insert_unique_data(self, prefixes, schema_name = "curated"):
        raw_data = self.extract_data(self.engine)
        unique_data = self.remove_duplicates(raw_data)
        split_dfs = self.split_dataframe_by_prefix(unique_data, prefixes.keys())

        # date_data.to_sql("raw_dates", self.engine, schema = schema_name, if_exists='append', index=False)
        # LOGGER.info("Inserted data into table raw_dates")
        for prefix, table_name in prefixes.items():
            split_dfs[prefix].to_sql(table_name, self.engine, schema = schema_name, if_exists='append', index=False)
            LOGGER.info(f"Inserted data in table {table_name}")
        LOGGER.info(f"All data saved succesfully")

        
