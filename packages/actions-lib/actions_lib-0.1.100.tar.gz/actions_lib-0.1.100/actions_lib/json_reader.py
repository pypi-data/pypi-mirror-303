import os
import json

class JSONReader:
    def __init__(self, base_dir = None):
        if base_dir is None:
            # Use the default path inside the library
            base_dir = os.path.dirname(__file__)
        self.base_dir = base_dir

    def read_json(self, subdirectory_name, file_name, file_suffix = '.json'):
        """
        Read the content of a JSON file based on the subdirectory name.
        
        :param subdirectory_name: Name of the subdirectory
        :return: Content of the JSON file parsed as a Python object
        :raises FileNotFoundError: If the JSON file does not exist
        :raises ValueError: If the JSON content cannot be parsed
        """
        # Construct the subdirectory path
        subdirectory_path = self.base_dir
        if subdirectory_name is not None:
            subdirectory_path = os.path.join(self.base_dir, subdirectory_name)
        # Construct the JSON file path
        if file_suffix is not None:
            json_file_path = os.path.join(subdirectory_path, f"{file_name}{file_suffix}")
        else:
            json_file_path = os.path.join(subdirectory_path, f"{file_name}")
        
        # Check if the JSON file exists
        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"JSON file not found: {json_file_path}")
        
        # Read and return the JSON file content
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            try:
                data = json.load(json_file)
                return data
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON file {json_file_path}: {str(e)}")