import os
import json
import importlib.resources as pkg_resources

def _load_config():
    # Check for the development config file first
    dev_path = os.path.join(os.path.dirname(__file__), 'config.json')
    
    if os.path.exists(dev_path):
        try:
            with open(dev_path, 'r') as f:
                config = json.load(f)
            return config['paths']  # Return all paths as a dictionary
        except (KeyError, json.JSONDecodeError):
            print("Error loading configuration. Using default paths.")
            return get_default_paths()  # Fallback to default paths
    else:
        # Fallback to package resource loading
        return load_config_from_package()

def load_config_from_package():
    try:
        with pkg_resources.open_text('rotational_placement', 'config.json') as f:
            config = json.load(f)
        return config['paths']  # Return all paths
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print("Error loading configuration from package. Using default paths.")
        return get_default_paths()

def get_default_paths():
    return {
        "plot_save_path": "./plots",
        "data_files_save_path":"./data_files"
    }
