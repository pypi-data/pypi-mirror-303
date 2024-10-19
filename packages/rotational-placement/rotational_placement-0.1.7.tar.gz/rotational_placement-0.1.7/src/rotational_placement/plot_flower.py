from .experiment_class import Experiment
def plot_flower(experiment: Experiment, max_radius=0):
    """
    Description
    -----------
    plots a circle of either specified radius or the max radius of given experiment and saves that as a flower plot

    PARAMETERS
    ----------
    experiment: Experiment
        instance with seed_data that is to be visualized
    max_radius: int
        default is 0, if specified max_radius is desired input max_radius

    RETURNS
    -------
    The function saves the plot at specified location (default is ./plots/flower_plots/)
    """

    if max_radius == 0: 
        max_radius = experiment.get_max_radius()
    
    from .load_config import load_config
    root_path = load_config().get("plot_save_path","plots")

    name = f"flower-{experiment.get_meta_data['alias']}-{max_radius}.png"
    path = f'{root_path}/flower_plots/{name}'

    import matplotlib.pyplot as plt
    _,ax = plt.subplots()

    ax.set_ylim(-max_radius * 1.1, max_radius * 1.1)
    ax.set_xlim(-max_radius * 1.1, max_radius * 1.1)

    ax.set_aspect('equal',adjustable='box')
    ax.set_axis_off()

    ax.add_patch(plt.Circle((0,0),max_radius,fill=False,color='k'))

    print('...creating plot...')

    for seed in experiment.getSeedData(): 
        if seed["distance"] > max_radius:
            break
        ax.add_patch(plt.Circle(seed,1,fill=True,color='k'))


    plt.savefig(path)    
    print(f"flower saved at {path}")

    