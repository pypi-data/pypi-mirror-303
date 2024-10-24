from ..utils import make_request
from ..logger import get_logger
from ..utils import make_request
from .quantities import Quantities 
import json

class Models:
    def __init__(self, config):
        self.config = config
        self.endpoint = f"{self.config.base_url}/api/computable-models"
        self.logger = get_logger(self.__class__.__name__)
        self.headers = {'Authorization': f'Bearer {self.config.load_token()}', 'Content-Type': 'application/json'}
        self.physical_quantities = Quantities(config)  # Delegate handling to the PhysicalQuantities class

    def list(self, params=None):
        """
        Retrieve a list of models with the same query parameters as the command-line client.
        :param params: Optional dictionary of query parameters.
        :return: List of models (dictionary containing model details).
        """
        headers = {'Authorization': f'Bearer {self.config.load_token()}'}
        # Define the same query parameters used in the command-line client
        default_params = {
            'search': '',
            'size': 50,
            'sort': 'updateDate,desc',
            'page': 0,
            'statuses': 'DRAFT,RELEASED'
        }

        # Merge any additional params provided with the default ones
        if params:
            default_params.update(params)

        self.logger.info("Fetching list of models with query parameters...")
        
        try:
            # Make request to the API endpoint with proper query params
            response = make_request('GET', self.endpoint, headers=headers, params=default_params, timeout=self.config.timeout)
            
            # Handle the response and ensure the 'content' field contains models
            if 'content' in response:
                return response['content']  # Return the list of models
            else:
                self.logger.error("Unexpected response format when fetching models.")
                return []
        except Exception as e:
            self.logger.error(f"Error fetching models: {e}")
            return []


    def get_model_dict(self):
        """
        Returns a dictionary mapping valid model names to their IDs.
        :return: Dictionary where keys are model names and values are model IDs.
        """
        models = self.list()
        
        # Create a dictionary of model names and their IDs
        model_dict = {model['kpiName']: model['id'] for model in models if 'kpiName' in model and 'id' in model}
        
        self.logger.info("Generated model dictionary with names and IDs.")
        return model_dict

    def get(self, model_id):
        """
        Retrieve details of a specific model.
        :param model_id: ID of the model.
        :return: Dictionary containing model details.
        """
        headers = {'Authorization': f'Bearer {self.config.load_token()}'}
        url = f"{self.endpoint}/{model_id}?deleted=false"
        self.logger.info(f"Fetching model with ID {model_id}...")

        try:
            # Make request to fetch the specific model details
            response = make_request('GET', url, headers=headers, timeout=self.config.timeout)
            return response
        except Exception as e:
            self.logger.error(f"Error fetching model details for ID {model_id}: {e}")
            return None
        
    # functions for importing models from JSON files
        
    def import_model_from_json(self, file_path):
        """
        Import a model from a JSON file, handling the physical quantities and units mapping.
        """
        with open(file_path, 'r') as f:
            model_data = json.load(f)

        # Delegate physical quantity handling to the PhysicalQuantities class
        model_data = self.physical_quantities.handle_physical_quantities(model_data)
        self.create_model(model_data)

    def create_model(self, model_data):
        """
        Create a new model with the updated model data.
        """
        self.logger.info(f"Attempting to create model: {model_data.get('kpiName')}")

        try:
            # Make the POST request to create the model and get both the response object and JSON data
            response, response_data = make_request('POST', self.endpoint, headers=self.headers, json=model_data)

            if response:
                status_code = response.status_code

                if status_code == 201:
                    self.logger.info(f"Model '{model_data.get('kpiName')}' created successfully!")
                elif status_code == 200:
                    self.logger.info(f"Model '{model_data.get('kpiName')}' updated or already existed.")
                else:
                    # If there is an error status code, log the error response content
                    error_message = response_data if response_data else response.text
                    self.logger.error(f"Error during model creation: {error_message}")

            else:
                self.logger.error(f"Model creation failed for '{model_data.get('kpiName')}': No response received.")

        except Exception as e:
            self.logger.error(f"Error during model creation: {e}")

    
    # functions for exporting models to JSON files

    def fetch_model_details(self, model_id):
        """
        Fetch details of a specific model from the API.
        
        Args:
            model_id (int): The ID of the model to fetch.
        
        Returns:
            dict: The model details, or None if the request fails.
        """
        url = f"{self.endpoint}/{model_id}?deleted=false"
        self.logger.info(f"Fetching details for model ID: {model_id}")
        
        try:
            # Expecting only a single return value from make_request (the response data)
            response_data = make_request('GET', url, headers=self.headers)
            if response_data:
                self.logger.info(f"Successfully fetched model details for ID: {model_id}")
                return response_data
            else:
                self.logger.error(f"Failed to fetch model details.")
                return None
        except Exception as e:
            self.logger.error(f"Error fetching model details: {e}")
            return None


    def convert_to_importable_format(self, api_response):
        """
        Converts the fetched model details into an importable JSON structure.
        
        Args:
            api_response (dict): The API response containing the model details.
        
        Returns:
            dict: The reformatted model ready for export, or None on error.
        """
        if not api_response:
            self.logger.error("No valid model data to convert.")
            return None

        # Create the structure for the importable model
        importable_model = {
            "engineType": api_response.get("engineType"),
            "kpiName": api_response.get("kpiName"),
            "abbr": api_response.get("abbr"),
            "calculationStyle": api_response.get("calculationStyle"),
            "status": "DRAFT",  # Default to DRAFT for export, can be modified later
            "description": api_response.get("description", ""),
            "script": api_response.get("script", "")
        }

        # Process inputs
        importable_model["inputs"] = [
            {
                "name": input_item.get("name"),
                "order": idx,
                "physicalQuantityUnit": {
                    "name": input_item["physicalQuantityUnit"].get("name"),
                    "unit": input_item["physicalQuantityUnit"].get("unit"),
                    "status": input_item["physicalQuantityUnit"].get("status")
                },
                "description": input_item.get("description", "")
            } for idx, input_item in enumerate(api_response.get("inputs", []))
        ]

        # Process outputs
        importable_model["outputs"] = [
            {
                "name": output_item.get("name"),
                "order": idx,
                "physicalQuantityUnit": {
                    "name": output_item["physicalQuantityUnit"].get("name"),
                    "unit": output_item["physicalQuantityUnit"].get("unit"),
                    "status": output_item["physicalQuantityUnit"].get("status")
                },
                "description": output_item.get("description", "")
            } for idx, output_item in enumerate(api_response.get("outputs", []))
        ]

        return importable_model

    def export_model_to_json(self, model_id, output_file):
        """
        Export a model to a JSON file based on the model's ID.
        
        Args:
            model_id (int): The ID of the model to export.
            output_file (str): The output file path for the exported JSON.
        """
        self.logger.info(f"Exporting model with ID {model_id} to {output_file}...")

        # Fetch model details
        model_details = self.fetch_model_details(model_id)
        if not model_details:
            self.logger.error(f"Failed to fetch model details for ID {model_id}.")
            return

        # Convert model details to an importable format
        importable_json = self.convert_to_importable_format(model_details)
        if not importable_json:
            self.logger.error(f"Failed to convert model to importable format for ID {model_id}.")
            return

        # Export the model to a JSON file
        try:
            with open(output_file, 'w') as json_file:
                json.dump(importable_json, json_file, indent=4)
            self.logger.info(f"Model ID {model_id} exported successfully to {output_file}.")
        except IOError as e:
            self.logger.error(f"Failed to write model to JSON file: {e}")