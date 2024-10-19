import os

def make_plot_dir():
    """
    Description
    -----------
    creates a plots directory and sub-directories with apt names in current repo
    """
    # Define the subdirectories to create under 'plots'
    subfolders = ["density_plots", "flower_plots", "heatmaps"]
    
    # Create the base directory
    os.makedirs("plots", exist_ok=True)
    
    # Loop over each subfolder and create it inside the base directory
    for folder in subfolders:
        folder_path = os.path.join("plots", folder)
        os.makedirs(folder_path, exist_ok=True)