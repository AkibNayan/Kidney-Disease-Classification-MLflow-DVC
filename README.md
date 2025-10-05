# Kidney-Disease-Classification-MLflow-DVC

Here I have used small set of data, that's why accuracy will be lower.

## Project Sequentiality

GitHub Repo -> project template -> requirements and setup -> logging, exception & utils module -> data ingestion notebook experiment -> data ingestion modular code -> prepare base model notebook experiment -> prepare base model modular code -> model training notebook experiment.

## Workflows Part

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/AkibNayan/Kidney-Disease-Classification-MLflow-DVC
```

### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv kidneyEnv
```

```bash
source kidneyEnv/Scripts/activate
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd

- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

## About MLflow & DVC

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & taging your model

DVC

- Its very lite weight for POC only
- lite weight expriements tracker
- It can perform Orchestration (Creating Pipelines)
