import json
import os
import importlib.resources as pkg_resources

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_data = self._load_config()
        self._validate_config()

    def _load_config(self):
        """Load configuration data from the JSON file."""
        try:
            # Access the configuration file as a resource within the current package
            with pkg_resources.files(__package__).joinpath(self.config_file).open('r') as f:
                config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
              
        return config

    def _validate_config(self):
            """Ensure PROJECT_DB_PATH is set, and prompt for it if missing."""
            if not self.config_data.get("PROJECT_DB_PATH"):
                print("PROJECT_DB_PATH is not set. Please provide the database path.")
                db_path = input("Enter the full path to the project database: ").strip()
                self.update_config("PROJECT_DB_PATH", db_path)
            
            # After attempting to update, check again and raise an exception if still not set
            if not self.config_data.get("PROJECT_DB_PATH"):
                raise ValueError("PROJECT_DB_PATH is not set. Please configure it before proceeding.")
    
    def get_config(self):
        """Return the current configuration as a dictionary."""
        return self.config_data

    def update_config(self, key, value):
        """Update the configuration in memory and on disk."""
        self.config_data[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config_data, f, indent=4)
    
    def get_variable(self, key):
        """Retrieve a specific configuration variable."""
        return self.config_data.get(key)

    def set_project_db_path(self, path):
        """Set the PROJECT_DB_PATH and validate it."""
        if not os.path.exists(path):
            raise ValueError(f"Database path {path} does not exist.")
        self.update_config("PROJECT_DB_PATH", path)
