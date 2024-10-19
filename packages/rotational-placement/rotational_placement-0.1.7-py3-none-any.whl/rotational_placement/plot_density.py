from .experiment_class import Experiment

def plot_density(aliass:list[str], *experiments: Experiment):
    """
    DESCRIPTION
    -----------
    Plot densities for multiple experiments, only including the common radius range.
    
    PARAMETERS
    ----------
    aliass: list[str]
        list of labels for data sets
    experiments: Experiment instances
        Instances of the Experiment class.
        
    RETURNS 
    -------
    The function saves the plot at specified location (default is ./plots/density_plots/)
    """

    import matplotlib.pyplot as plt
    import numpy as np
    import os

    # Find the maximum common radius across all experiments
    max_common_radius = min([max(exp.getRadius()) for exp in experiments])

    # Construct the name for saving the plot
    name = 'density-' + '-'.join([exp.getMetaData()['alias'] for exp in experiments]) + '.svg'
    path = f'plots/densityPlots/{name}'

    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Create the plot
    f, ax = plt.subplots(1)
    
    # Loop through each experiment instance
    for i,exp in enumerate(experiments):
        radius = np.array(exp.getRadius())
        efficacy = np.array(exp.getEfficacy())
        
        # Filter data to only include points within the common radius
        valid_indices = radius <= max_common_radius
        truncated_radius = radius[valid_indices]
        truncated_efficacy = efficacy[valid_indices]
        
        # Calculate density for the truncated data
        density = truncated_efficacy / (truncated_radius ** 2)
        
        # Plot with the alias as the label
        ax.plot(truncated_radius, density, label=aliass[i])
    
    # Set axis limits
    ax.set_ylim(ymin=0, ymax=1.05)
    ax.set_xlim(xmin=0, xmax=max_common_radius)
    
    # Adjust plot appearance
    for spine in ["bottom", "left", "top", "right"]:
        ax.spines[spine].set_linewidth(1.1)

    # Add legend
    ax.legend()
    

    plt.savefig(path)
    print(f"plot saved at {path}")
