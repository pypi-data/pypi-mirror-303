import json
import os
import importlib.resources as pkg_resources

class ConfigManager:
    def __init__(self, config_file='mega_pack_pbf_parser_config.json', default_config_file='default_config.json'):
        self.user_config_path = os.path.join(os.path.expanduser("~"), config_file)
        self.default_config_file = default_config_file
        self.config_data = self._load_or_create_user_config()
        self._validate_config()

    def _load_or_create_user_config(self):
        """Load the user configuration or create it from package defaults if missing."""
        if os.path.exists(self.user_config_path):
            # Load existing user config
            with open(self.user_config_path, 'r') as f:
                return json.load(f)
        else:
            # Load defaults from the package and save to user config
            default_config = self._load_default_config()
            with open(self.user_config_path, 'w') as f:
                json.dump(default_config, f, indent=4)
            print(f"*** Saved project config file to {self.user_config_path}")
            print(f"*** Update this file whenever any of the values change.")
            return default_config

    def _load_default_config(self):
        """Load default configuration from the package's default_config.json."""
        try:
            with pkg_resources.files(__package__).joinpath(self.default_config_file).open('r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Default configuration file {self.default_config_file} not found in the package.")
        
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
        """Update the configuration in memory and save it to the user config file."""
        self.config_data[key] = value
        with open(self.user_config_path, 'w') as f:
            json.dump(self.config_data, f, indent=4)

    def get_variable(self, key):
        """Retrieve a specific configuration variable."""
        return self.config_data.get(key)

    def set_project_db_path(self, path):
        """Set the PROJECT_DB_PATH and validate it."""
        if not os.path.exists(path):
            raise ValueError(f"Database path {path} does not exist.")
        self.update_config("PROJECT_DB_PATH", path)
