import pandas as pd
import requests
import logging

LOGGER = logging.getLogger(__name__)

class ApiHandler:
    """Class for API Handling Functionalities."""
    def __init__(self):
        self.api_url = "https://my.api.mockaroo.com/policy_sales.json?key=07cac880"   # TODO: Add the config file

    def fetch_data(self):
        """
        Extract data from an API.

        Args:
            api_url (str): URL of the API endpoint.

        Returns:
            pandas.DataFrame: DataFrame containing the extracted data.
        """
        LOGGER.info("fetching new data...")
        try:
            response = requests.get(self.api_url)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            data = response.json()
            LOGGER.info("data was successfully retrieved.")
            # Check if data is a dictionary or a list 
            if isinstance(data, list):     
                data = data[0]             # If data is a list, assume it contains only one element
            # Initialize an empty DataFrame
            dfs = list(map(lambda category: pd.json_normalize(data[category]).add_prefix(category+'_'), data)) 
            # Concatenate the flattened DataFrames
            df = pd.concat(dfs, axis=1)    
            return df
        except requests.RequestException as e:
            LOGGER.error("Error extracting data from API", exc_info=True)
            return None