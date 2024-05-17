import pandas as pd
import logging
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
    
    # columns = [vehicles_vehicle_key, vehicles_registration_type,.....]
    # split_dfs = {'vehicles': df[columns], }
    
    def insert_data(self, df, prefixes, schema_name):
        """Insert the split DataFrames into their respective tables."""
        split_dfs = self.split_dataframe_by_prefix(df, prefixes.keys())
        for prefix, table_name in prefixes.items():
            split_dfs[prefix].to_sql(table_name, self.engine, schema = schema_name, if_exists='append', index=False)
            LOGGER.info(f"Inserted data into table {table_name}")
        LOGGER.info("All data has been successfully saved to PostgreSQL!")

        
