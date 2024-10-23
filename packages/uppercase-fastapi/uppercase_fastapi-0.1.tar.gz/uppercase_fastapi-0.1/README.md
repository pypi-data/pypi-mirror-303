# DEMO FastAPI project 

## Requirements
* Python 3.10+
+ AWS Access credentials

## Creating and Starting a Virtual Environment
Best way to download the required python packages and run the app locally is to start a virtual environment

pip install virtualenv
python -m venv <virtual-environment-name>
source <virtual-environment-name>/bin/activate

## Downloading Required Libraries
pip install -r requirements.txt

## Running Unit Tests
aws-vault-windows-386.exe exec sg-dev-ds -- pytest <filename>

## Running App Locally
aws-vault-windows-386.exe exec sg-dev-ds -- uvicorn <filename>:app --reload


