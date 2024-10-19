# Rotational Placement

A package for generating and visualizing data related to rotational placement.

### Initial setup
Using pip: `pip install rotational_placement`

### Experiment class

create an Experiment instance

`exp = Experiment(alias="1.pi",a=113,b=355,step_size=1,experiment_type="num")`

generate data and save it to a file

`exp.run_experiment(151)`

`exp.write_to_file()`

read experiment instance from a file

`exp = Experiment.read_from_file(alias="1.pi",a=113,b=355,step_size=1,experiment_type="num")`

The Experiment class also has a number of getter methods, the following are included: 

`.get_meta_data()`

`.get_max_radius()`

`.get_density_data()`

`.get_radius_data()`

`.get_seed_data()`

`.get_efficacy_data()`

## Plotting

The following plots are included as of now: 

They save the plots at the location specified in config.json.

`plot_density(alias_list=['num','sym','ff'],*experiments=ff_exp,num_exp,sym_exp)`

