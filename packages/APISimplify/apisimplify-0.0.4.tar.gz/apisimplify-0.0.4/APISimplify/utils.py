import time
import requests
import json
import jsonschema
from jsonschema import validate
from requests.exceptions import HTTPError

class Utils:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print(f"Data saved to {filename}")

    def load_from_json(filename):
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                print(f"Data loaded from {filename}")
                return data
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
            return None
        
    def get_current_timestamp():
        return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

    def validate_json(json_data, schema):
        try:
            validate(instance=json_data, schema=schema)
            return True, ""
        except jsonschema.exceptions.ValidationError as ve:
            return False, ve.message