from configparser import ConfigParser

CONFIG_PATH_VAR = "src/config/config.ini"

class ConfigHandler:
    """Class for Config Hanlder Functionalities."""
    def __init__(self):
        self.config_path = CONFIG_PATH_VAR
        self.config = ConfigParser()
        self.config.read(self.config_path)

    def get_api_url(self, api_name):
        """Extracts API Url from config file."""
        return self.config.get(api_name, 'url')
    
