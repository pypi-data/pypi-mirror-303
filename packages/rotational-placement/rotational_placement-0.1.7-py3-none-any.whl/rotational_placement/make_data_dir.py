import os

def make_data_dir():
    """
    Description
    -----------
    creates a data_files directory and sub-directories with apt names in current repo
    """
    # Define the main folders to create
    subfolders = ["num", "ff", "sym"]
    
    # Create the base directory
    os.makedirs("data_files", exist_ok=True)
    
    # Loop over each folder and create it inside the base directory
    for folder in subfolders:
        folder_path = os.path.join("data_files", folder)
        os.makedirs(folder_path, exist_ok=True)