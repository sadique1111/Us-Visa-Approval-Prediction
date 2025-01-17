import os
from pathlib import Path

# why we use pathlib. It handles the / and \ slash in the path directory in any OS. windows machine has \ slash in the folder directory

# First ctreate the main folder us_visa which is the project name (parent folder) and create constructor file as local package

project_name ="us_visa"

# second create the sub folder under the main folder as list+of_files.each folder will have their own constructor file.

list_of_files = [
 f"{project_name}/__init__.py",
 f"{project_name}/components/__init__.py",
 f"{project_name}/components/data_ingestion.py",
 f"{project_name}/components/data_validation.py",
 f"{project_name}/components/data_transformation.py",
 f"{project_name}/components/model_training.py",
 f"{project_name}/components/model_evaluation.py",
 f"{project_name}/components/model_pusher.py",
 f"{project_name}/configuration/__init__.py",
 f"{project_name}/configuration/__init__.py",
 f"{project_name}/constant/__init__.py",
 f"{project_name}/entity/__init__.py",
 f"{project_name}/entity/config_entity.py",
 f"{project_name}/entity/artifact_entity.py",
 f"{project_name}/exception/__init__.py",
 f"{project_name}/logger/__init__.py",
 f"{project_name}/pipeline/__init__.py",
 f"{project_name}/pipeline/training_pipeline.py",
 f"{project_name}/pipeline/prediction_pipeline.py",
 f"{project_name}/utils/__init__.py",
 f"{project_name}/utils/main_utils.py",
 "app.py",
 "config/model.yaml",
 "config/schema.yaml",
 "Dockerfile",
 ".dockerignore",
 "demo.py",
 "requirements.txt",
 "setup.py"
]

# function to create the list of files mentioned above.

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")