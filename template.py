import os
from pathlib import Path
import logging

# logging Configuration
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s: %(levelname)s: %(message)s:",
                    datefmt="%Y-%m-%d %H:%M:%S")

project_name = "kidneyDiseasePrediction"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directories {filedir}, for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filename}")
    
    else:
        logging.info(f"{filename} already exists")



"""
list_of_files: List containing all file paths to be created
.github/workflow/.gitkeep: GitHub Actions workflow directory (.gitkeep ensures empty directory is tracked by Git)
f"src/{project_name}/__init__.py": f-string that inserts project_name variable into the path
__init__.py: Makes Python treat directories as packages (enables imports)
Structure breakdown:

components/ - Modular components of the application
utils/ - Utility/helper functions
config/ - Configuration files and settings
pipeline/ - ML pipeline stages
entity/ - Data classes/entities
constants/ - Constant values used across project
config.yaml - YAML configuration file
dvc.yaml - Data Version Control pipeline definition
params.yaml - Parameters for ML experiments
requirements.txt - Python dependencies
setup.py - Package installation script
research/trials.ipynb - Jupyter notebook for experimentation
templates/index.html - HTML template for web interface

"""