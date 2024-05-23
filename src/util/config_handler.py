from configparser import ConfigParser

CONFIG_PATH_VAR = "src/config/config.ini"

class ConfigHandler:
    """Class for Config Hanlder Functionalities."""
    def __init__(self):
        self.config_path = CONFIG_PATH_VAR
        self.config = ConfigParser()
        self.config.read(self.config_path)

    def get_api_url(self, api_name):
        """Extracting API Url from config file."""
        return self.config.get(api_name, 'url')
    
    def get_db_params(self, db_name):
        """Extracting the db params from config file"""
        return {param: self.config.get(db_name, param) for param in self.config.options(db_name)}
    
    def get_prefixes(self, prfx_name):
        """Extracting the prefixes from config file"""
        return eval(self.config.get(prfx_name, 'prefixes'))
    
    def get_raw_data_query(self, query_name):
        """Extracting the query from config file"""
        return self.config.get(query_name, 'query')
    
    def get_tables_names(self, tables):
        """Extracting the tables names from config file"""
        return eval(self.config.get(tables, 'tables'))