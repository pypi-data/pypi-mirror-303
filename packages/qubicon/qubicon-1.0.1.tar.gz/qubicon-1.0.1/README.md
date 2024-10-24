# Qubicon Python Library

**Qubicon Python Library** is a Python interface that allows users to interact with Qubicon's bioprocess management platform programmatically. It offers tools for managing models, physical quantities, and processes, making it easier to automate complex tasks on the platform, streamline data acquisition, and integrate bioprocess data into various workflows.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Authentication](#authentication)
4. [Key Features](#key-features)
   - [Models Management](#models-management)
   - [Physical Quantities Management](#physical-quantities-management)
   - [Processes and Data Extraction](#processes-and-data-extraction)
5. [Functionality Overview](#functionality-overview)
   - [Models](#models)
   - [Processes](#processes)
   - [Quantities](#quantities)
6. [Usage Examples](#usage-examples)
7. [License](#license)

---

## Installation

To install the Qubicon Python Library, simply use pip:

```bash
pip install qubicon
```

---

## Configuration

After installation, configure the library by setting your base URL and any necessary credentials.

### Example Configuration:

```python
from qubicon import Config

config = Config(base_url='https://master.qub-lab.io/')
```

---

## Authentication

To authenticate with the Qubicon API, you need valid credentials (username and password). The `authenticate` method helps you securely log in to the API.

### Example Authentication:

```python
from qubicon import authenticate

# Authenticate with the API
authenticate(config, username='your_username', password='your_password')
```

---

## Key Features

### 1. **Models Management**

Manage computational models, import/export models, and retrieve details from the Qubicon API. The `Models` class provides several methods to interact with models stored in the Qubicon system.

---

## Functionality Overview

### Models

The `Models` class allows you to manage models by listing, retrieving, exporting, and importing them.

#### `list()`
Retrieves a list of all models available in the system.

```python
from qubicon.api.models import Models

# Initialize the Models class
models = Models(config)

# List all models
model_list = models.list()
for model in model_list:
    print(f"ID: {model['id']}, Name: {model['kpiName']}, Status: {model['status']}")
```

#### `get(model_id)`
Retrieve the details of a specific model using its ID.

```python
# Fetch a specific model by its ID
model_id = 123
model_details = models.get(model_id)
print(f"Model Name: {model_details['kpiName']}, Status: {model_details['status']}")
```

#### `get_model_dict()`
Returns a dictionary mapping model names to their IDs.

```python
# Get a dictionary of model names and their IDs
model_dict = models.get_model_dict()
print(model_dict)
```

#### `import_model_from_json(file_path)`
Imports a model from a JSON file.

```python
# Import a model from a JSON file
models.import_model_from_json('path_to_model.json')
```

#### `export_model_to_json(model_id, output_file)`
Exports a model to a JSON file.

```python
# Export a model to a JSON file
models.export_model_to_json(423, 'exported_model.json')
```

---

### Processes

The `Processes` class provides methods to handle process data, including listing processes, retrieving channels, and extracting data.

#### `list_processes()`
Lists all available processes in the system.

```python
from qubicon.api.processes import Processes

# Initialize the Processes class
processes = Processes(config)

# List all processes
process_list = processes.list_processes()
for process in process_list:
    print(f"Process ID: {process['id']}, Name: {process['name']}")
```

#### `list_process_channels(process_id)`
Lists all channels associated with a specific process.

```python
# List channels for a specific process
process_id = 123
channels = processes.list_process_channels(process_id)
for channel in channels:
    print(f"Channel ID: {channel['id']}, Name: {channel['name']}")
```

#### `extract_process_data(process_id, selected_channels, start_date, end_date, granularity, output_file, output_format)`
Extracts process data for the selected channels and saves it to a file (JSON or CSV).

```python
# Extract process data and save it as a CSV file
selected_channels = [{'id': 1}, {'id': 2}]
start_date = '1728622700000'
end_date = '1728624500000'

processes.extract_process_data(
    process_id=123,
    selected_channels=selected_channels,
    start_date=start_date,
    end_date=end_date,
    granularity=60,
    output_file='process_data.csv',
    output_format='csv'
)
```

#### `get_process_details(process_id)`
Retrieves the start and end dates of a process by its ID.

```python
# Get process details
start_date, end_date = processes.get_process_details(123)
print(f"Process Start: {start_date}, Process End: {end_date}")
```

---

### Quantities

The `Quantities` class allows you to manage physical quantities and units on the Qubicon platform.

#### `list()`
Retrieves a list of all physical quantities available in the system.

```python
from qubicon.api.quantities import Quantities

# Initialize the Quantities class
quantities = Quantities(config)

# List all physical quantities
quantity_list = quantities.list()
for quantity in quantity_list:
    print(f"Quantity ID: {quantity['id']}, Name: {quantity['name']}")
```

#### `get(quantity_id)`
Retrieves the details of a specific physical quantity by its ID.

```python
# Get details of a specific quantity
quantity_id = 71
quantity_details = quantities.get(quantity_id)
print(f"Quantity Name: {quantity_details['name']}, Unit: {quantity_details['units'][0]['unit']}")
```

#### `create_physical_quantity(pq_name, unit_name)`
Creates a new physical quantity with a specific unit.

```python
# Create a new physical quantity
new_quantity = quantities.create_physical_quantity('New Flow Rate', 'mL/min')
print(f"Created Quantity ID: {new_quantity['id']}")
```

#### `add_unit_to_existing_physical_quantity(pq_id, pq_name, unit_name)`
Adds a new unit to an existing physical quantity.

```python
# Add a new unit to an existing physical quantity
quantities.add_unit_to_existing_physical_quantity(71, 'Flow Rate', 'L/min')
```

#### `check_existing_physical_quantity(pq_name)`
Checks if a physical quantity already exists by performing a fuzzy match on the name.

```python
# Check if a physical quantity exists
existing_pq = quantities.check_existing_physical_quantity('Flow Rate')
if existing_pq:
    print(f"Found existing physical quantity: {existing_pq['name']}")
```

#### `check_existing_unit(physical_quantity, unit_name)`
Checks if a specific unit exists within a physical quantity.

```python
# Check if a unit exists for a physical quantity
existing_unit = quantities.check_existing_unit(existing_pq, 'L/min')
if existing_unit:
    print(f"Found existing unit: {existing_unit['unit']}")
```

#### `handle_physical_quantities(model_data)`
Handles the creation and updating of physical quantities and units for both inputs and outputs of a model.

```python
# Automatically handle physical quantities for a model
updated_model_data = quantities.handle_physical_quantities(model_data)
print("Updated model with physical quantities:", updated_model_data)
```

---

## Usage Examples

### Full Example: Exporting and Importing Models

```python
from qubicon import Config, authenticate
from qubicon.api.models import Models

# Configuration and authentication
config = Config(base_url='https://master.qub-lab.io/')
authenticate(config, username='yourusername', password='yourpassword')

# Initialize the Models class
models = Models(config)

# Export a model to JSON
models.export_model_to_json(423, 'exported_model.json')

# Import the model back into the system
models.import_model_from_json('exported_model.json')
```

### Full Example: Extracting Process Data

```python
from qubicon import Config, authenticate
from qubicon.api.processes import Processes

# Configuration and authentication
config = Config(base_url='https://master.qub-lab.io/')
authenticate(config, username='yourusername', password='yourpassword')

# Initialize the Processes class
processes = Processes(config)

# Define the process ID and selected channels
process_id = 123
selected_channels = [{'id': 1}, {'id': 2}]
start_date = '1728622700000'
end_date = '1728624500000'

# Extract and save data
processes.extract_process_data(
    process_id=process_id,
    selected_channels=selected_channels,
    start_date=start_date,
    end_date=end_date,
    granularity=148,
    output_file=processed_data.csv'

process_data.csv',
    output_format='csv'
)
```

---

## License

## License

This project is licensed under the Apache License, Version 2.0. You may not use this project except in compliance with the License.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

You can view the full text of the license at the following link:

[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

```