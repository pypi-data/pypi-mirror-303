from ..utils import make_request
from ..logger import get_logger
import pandas as pd

class Processes:
    def __init__(self, config):
        """
        Initializes the Processes class with the provided configuration.
        
        :param config: A Config object that contains the API base URL and authentication token.
        """
        self.config = config
        self.endpoint = f"{self.config.base_url}/public-api/processes"
        self.logger = get_logger(self.__class__.__name__)
        self.headers = {'Authorization': f'Bearer {self.config.load_token()}'}

    def list_processes(self):
        """
        Fetches and returns all available processes from the API. This method retrieves a list of processes 
        based on parameters like the number of processes to fetch, sorting order, and GMP status.

        :return: A list of processes in dictionary format, or None if the request fails.
        """
        params = {
            'size': 90,
            'sort': 'lastUsageDate,desc',
            'gmp': False,
            'archivedOrWillBeArchived': False,
            'partOfExperiment': False
        }
        
        try:
            self.logger.info("Fetching processes from the API...")
            response = make_request('GET', self.endpoint, headers=self.headers, params=params)
            processes = response.get('content', [])
            
            if processes:
                self.logger.info(f"Retrieved {len(processes)} processes.")
                return processes
            else:
                self.logger.warning("No processes available or invalid response format.")
                return None
        except Exception as e:
            self.logger.error(f"Error fetching processes: {e}")
            return None
        
    def list_process_channels(self, process_id):
        """
        Fetches and returns the channels associated with a specific process.

        :param process_id: The ID of the process whose channels should be retrieved.
        :return: A list of channels in dictionary format, or None if the request fails.
        """
        url = f"{self.config.base_url}/api/processes/{process_id}/channels"
        
        try:
            self.logger.info(f"Fetching channels for process ID: {process_id}")
            response = make_request('GET', url, headers=self.headers)
            
            if response:
                self.logger.info(f"Retrieved {len(response)} channels.")
                return response
            else:
                self.logger.warning(f"No channels available for process {process_id}.")
                return None
        except Exception as e:
            self.logger.error(f"Error fetching channels for process {process_id}: {e}")
            return None
        
    def extract_process_data(self, process_id, selected_channels, start_date, end_date, granularity, output_file, output_format="json"):
        """
        Extracts process data for the selected channels and saves it in the specified format (JSON or CSV).
        
        :param process_id: The ID of the process from which data is to be extracted.
        :param selected_channels: A list of dictionaries, each containing a channel ID.
        :param start_date: The start timestamp (in milliseconds) for data extraction.
        :param end_date: The end timestamp (in milliseconds) for data extraction.
        :param granularity: The granularity of the data to be fetched (e.g., every minute, hour).
        :param output_file: The file path where the extracted data will be saved.
        :param output_format: The format for saving the data, either 'json' or 'csv' (default is 'json').
        """
        url = f"{self.config.base_url}/api/charts/multiplex-data-channels"
        collected_data = []

        payload = {
            "channels": [
                {
                    "id": channel["id"],
                    "type": "ONLINE",
                    "startDate": start_date,
                    "endDate": end_date,
                    "granularity": granularity
                } for channel in selected_channels
            ]
        }

        try:
            self.logger.info(f"Fetching data for process ID: {process_id}")
            response = make_request('POST', url, json=payload, headers=self.headers)
            if response:
                for entry in response['channels']:
                    for value in entry['value']:
                        collected_data.append({
                            "time": value['time'],
                            "channel_id": entry['key']['id'],
                            "value": value['value']
                        })

                df = pd.DataFrame(collected_data)
                if output_format == "json":
                    df.to_json(output_file, orient='records', indent=4)
                    self.logger.info(f"Data successfully written to {output_file} in JSON format.")
                elif output_format == "csv":
                    df.pivot(index="time", columns="channel_id", values="value").to_csv(output_file)
                    self.logger.info(f"Data successfully written to {output_file} in CSV format.")
            else:
                self.logger.error(f"Failed to fetch data for process ID {process_id}.")
        except Exception as e:
            self.logger.error(f"Error extracting data for process {process_id}: {e}")

    def get_process_details(self, process_id):
        """
        Fetches the start and end dates of a specific process using its ID.
        If the process is still running, the end date is defaulted to 30 minutes after the start date.

        :param process_id: The ID of the process.
        :return: A tuple containing the start and end dates (in milliseconds) of the process.
        """
        url = f"{self.config.base_url}/public-api/processes/{process_id}"
        
        try:
            self.logger.info(f"Fetching details for process ID: {process_id}")
            response = make_request('GET', url, headers=self.headers)
            
            if response:
                start_date = response.get('startDate')
                end_date = response.get('endDate') or start_date + (30 * 60 * 1000)  # Default to 30 min after start
                self.logger.info(f"Process {process_id} start date: {start_date}, end date: {end_date}")
                return start_date, end_date
            else:
                self.logger.error(f"Failed to fetch details for process {process_id}.")
                return None, None
        except Exception as e:
            self.logger.error(f"Error fetching details for process {process_id}: {e}")
            return None, None
