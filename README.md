## Run the code from the root directory using:
`py -m src.app7`

## Requirements available in requirements.txt
`py -m pip install -r requirements.txt`

## Virtual Environment

##### To create a venv run:
`python -m venv .venv` from the root of the repo

##### To activate q venv run:

Windows (in GitBash): `source .venv/Scripts/activate`

##### To deactivate the venv run:
`deactivate` in the shell when the venv is active

## MySQL DB
Start in background: 
  - `docker-compose up -d` to run in the background
Start in active shell:
  - `docker-compose up` to run in the active shell
Stop: 
`docker-compose stop`