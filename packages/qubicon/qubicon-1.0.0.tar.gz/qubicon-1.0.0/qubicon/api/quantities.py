from ..utils import make_request
from ..logger import get_logger

class Quantities:
    def __init__(self, config):
        """
        Initializes the Quantities class with the provided configuration.
        
        :param config: A Config object that contains the API base URL and authentication token.
        """
        self.config = config
        self.endpoint = f"{self.config.base_url}/api/physical-quantities"
        self.logger = get_logger(self.__class__.__name__)
        self.headers = {'Authorization': f'Bearer {self.config.load_token()}'}
        
    def list(self):
        """
        Retrieves and returns a list of all physical quantities available in the system.

        :return: A list of physical quantities in dictionary format, or None if the request fails.
        """
        self.logger.info("Fetching list of physical quantities...")
        return make_request('GET', self.endpoint, headers=self.headers, timeout=self.config.timeout)

    def get(self, quantity_id):
        """
        Retrieves the details of a specific physical quantity by its ID.

        :param quantity_id: The ID of the physical quantity to retrieve.
        :return: A dictionary containing the physical quantity details, or None if the request fails.
        """
        url = f"{self.endpoint}/{quantity_id}"
        self.logger.info(f"Fetching physical quantity with ID {quantity_id}...")
        return make_request('GET', url, headers=self.headers, timeout=self.config.timeout)

    def normalize_name(self, name):
        """
        Normalizes a physical quantity name by removing special characters and converting it to lowercase.

        :param name: The name of the physical quantity.
        :return: A normalized version of the name.
        """
        import re
        return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

    def fuzzy_match(self, name1, name2, threshold=93):
        """
        Performs a fuzzy string matching between two physical quantity names.

        :param name1: The first name to compare.
        :param name2: The second name to compare.
        :param threshold: The similarity threshold for considering a match (default is 93%).
        :return: True if the similarity exceeds the threshold, False otherwise.
        """
        from rapidfuzz import fuzz
        normalized_name1 = self.normalize_name(name1)
        normalized_name2 = self.normalize_name(name2)
        similarity = fuzz.token_sort_ratio(normalized_name1, normalized_name2)
        return similarity >= threshold

    def check_existing_physical_quantity(self, pq_name):
        """
        Checks if a physical quantity with a similar name already exists in the system using fuzzy matching.

        :param pq_name: The name of the physical quantity to check.
        :return: The matching physical quantity if found, or None if no match is found.
        """
        response = make_request('GET', self.endpoint, headers=self.headers)
        if response and isinstance(response, list):
            for pq in response:
                if self.fuzzy_match(pq['name'], pq_name):
                    self.logger.info(f"Fuzzy match found: '{pq['name']}' matches '{pq_name}' (ID: {pq['id']}).")
                    return pq
        return None

    def check_existing_unit(self, physical_quantity, unit_name):
        """
        Checks if a specific unit exists within a given physical quantity.

        :param physical_quantity: The physical quantity dictionary.
        :param unit_name: The name of the unit to check.
        :return: The matching unit if found, or None if no match is found.
        """
        for unit in physical_quantity.get('units', []):
            if self.fuzzy_match(unit['unit'], unit_name):
                self.logger.info(f"Unit match found: '{unit_name}' in physical quantity '{physical_quantity['name']}'.")
                return unit
        return None

    def create_physical_quantity(self, pq_name, unit_name):
        """
        Creates a new physical quantity along with an initial unit.

        :param pq_name: The name of the physical quantity to create.
        :param unit_name: The name of the unit to associate with the new physical quantity.
        :return: The created physical quantity in dictionary format, or None if creation fails.
        """
        data = {"name": pq_name, "units": [{"unit": unit_name}]}
        response = make_request('POST', self.endpoint, headers=self.headers, json=data)
        if response and response.status_code in [200, 201]:
            self.logger.info(f"Physical quantity '{pq_name}' created successfully.")
            return response.json()
        else:
            self.logger.error(f"Failed to create physical quantity '{pq_name}'. Response: {response.content}")
            return None

    def add_unit_to_existing_physical_quantity(self, pq_id, pq_name, unit_name):
        """
        Adds a new unit to an existing physical quantity.

        :param pq_id: The ID of the existing physical quantity.
        :param pq_name: The name of the existing physical quantity.
        :param unit_name: The name of the unit to add.
        :return: The updated physical quantity in dictionary format, or None if the update fails.
        """
        url = f"{self.endpoint}/{pq_id}"
        existing_pq = self.check_existing_physical_quantity(pq_name)
        if not existing_pq:
            self.logger.error(f"Physical quantity '{pq_name}' not found.")
            return None

        new_unit = {"unit": unit_name, "physicalQuantityId": pq_id}
        existing_pq['units'].append(new_unit)
        response = make_request('PUT', url, headers=self.headers, json=existing_pq)
        if response and response.status_code == 200:
            self.logger.info(f"Unit '{unit_name}' added to physical quantity '{pq_name}'.")
            return response.json()
        else:
            self.logger.error(f"Failed to add unit to physical quantity '{pq_name}'.")
            return None

    def handle_physical_quantities(self, model_data):
        """
        Processes and ensures all physical quantities and units in the model data exist in the system. 
        If a physical quantity or unit doesn't exist, it is created.

        :param model_data: A dictionary containing the model's inputs and outputs.
        :return: The updated model data with physicalQuantityId and unit ID populated.
        """
        for var in model_data.get('inputs', []) + model_data.get('outputs', []):
            pq_name = var['physicalQuantityUnit']['name']
            unit_name = var['physicalQuantityUnit']['unit']

            existing_pq = self.check_existing_physical_quantity(pq_name)
            if existing_pq:
                var['physicalQuantityUnit']['physicalQuantityId'] = existing_pq['id']
                existing_unit = self.check_existing_unit(existing_pq, unit_name)
                if not existing_unit:
                    updated_pq = self.add_unit_to_existing_physical_quantity(existing_pq['id'], pq_name, unit_name)
                    if updated_pq:
                        new_unit = next((u for u in updated_pq['units'] if u['unit'] == unit_name), None)
                        if new_unit:
                            var['physicalQuantityUnit']['id'] = new_unit['id']
            else:
                new_pq = self.create_physical_quantity(pq_name, unit_name)
                if new_pq:
                    var['physicalQuantityUnit']['physicalQuantityId'] = new_pq['id']
                    var['physicalQuantityUnit']['id'] = new_pq['units'][0]['id']

        return model_data
