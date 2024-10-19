import os

class Experiment: 
    def __init__(self, alias: str, a: int, b: int, step_size: int, experiment_type: str): 
        from .load_config import load_config
        
        self.alias = str(alias)
        self.a = int(a)
        self.b = int(b)
        self.step_size = int(step_size)
        self.experiment_type = str(experiment_type)

        # Load configuration
        config = load_config()
        root_path = config.get("data_files_path", "data_files")  # Default to "data_files" if not set in config

        # Define name and path for saving results
        self.name = f"{self.alias}-{self.a},{self.b}-{self.step_size}-{self.experiment_type}.txt"
        self.path = os.path.join(root_path, self.experiment_type, self.alias, self.name)

        # Initialize seed_data and density_data based on experiment type
        if experiment_type in ["num", "sym"]:
            self.seed_data = []
        self.density_data = {"efficacy": [], "radius": []}

        # Ensure directories exist
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
    
    def run_experiment(self, max_radius: int) -> None:
        from ._rp_num import _rp_num
        from ._rp_ff import _rp_ff
        #from .__rp_sym__ import __rp_sym__

        match self.experiment_type: 
            case "num":
                self.density_data, self.seed_data = _rp_num(self.a, self.b, self.step_size, max_radius, self)
            case "ff":
                self.density_data = _rp_ff(self.a, self.b, self.step_size, max_radius, self)
            case "sym":
                pass 
                #self.density_data, self.seed_data = __rp_sym__(self.a, self.b, self.step_size, max_radius, self)
            case _:
                raise ValueError("invalid experiment type")
        print("Experiment done and added to instance")

    def write_to_file(self) -> None:
        with open(self.path, "w") as file:
            file.write(f"alias:{self.alias}\n")
            file.write(f"a:{self.a}\n")
            file.write(f"b:{self.b}\n")
            file.write(f"step_size:{self.step_size}\n")
            file.write(f"experiment_type:{self.experiment_type}\n")
            
            file.write("--- Seed Data ---\n")
            for seed in self.seed_data:
                file.write(f"{seed}\n")
            
            file.write("--- Density Data ---\n")
            for efficacy, radius in zip(self.density_data["efficacy"], self.density_data["radius"]):
                file.write(f"{efficacy},{radius}\n")
        
        print("Data written to file")

    def get_meta_data(self) -> dict[str,int|str]:
        return {'alias': self.alias,
                'a': self.a,
                'b': self.b,
                'experimentType': self.experiment_type,
                'step_size': self.step_size,
                'max_radius': self.get_max_radius()}

    def get_max_radius(self) -> int: 
        try: 
            return int(self.density_data["radius"][-1])
        except IndexError:
            print("seed_data is empty")
            return None
    
    def get_density(self) -> list[float]: 
        return [float(e) / (float(r) ** 2) for e, r in zip(self.density_data['efficacy'], self.density_data['radius'])]

    def get_seed_data(self) -> list[dict[str,float|int]]: 
        return self.seed_data
        
    def get_radius(self) -> list[int]:
        return self.density_data["radius"]

    def get_efficacy(self) -> list[int]:
        return self.density_data["efficacy"]
        
    @staticmethod
    def read_from_file(alias: str, a: int, b: int, step_size: int, experiment_type: str):
        import rotational_placement.load_config as load_config
        
        # Load configuration for the path
        config = load_config()
        root_path = config.get("data_files_path", "data_files")  # Default to "data_files" if not set in config

        # Create the file name and path
        name = f'{alias}-{a},{b}-{step_size}-{experiment_type}.txt'
        path = os.path.join(root_path, experiment_type, alias, name)

        seed_data = []
        density_data = {'efficacy': [], 'radius': []}
        section = None

        # Read the data from the file
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line == '--- Seed Data ---':
                    section = 'seed_data'
                elif line == '--- Density Data ---':
                    section = 'density_data'
                elif section == 'seed_data':
                    seed_data.append(line)
                elif section == 'density_data':
                    if line:  # Avoid empty lines
                        efficacy, radius = map(float, line.split(','))
                        density_data['efficacy'].append(efficacy)
                        density_data['radius'].append(radius)

        # Create and return an Experiment instance
        experiment = Experiment(alias, a, b, step_size, experiment_type)
        experiment.seed_data = seed_data
        experiment.density_data = density_data
        return experiment
