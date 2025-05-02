# Dummy bot

## Create image

docker build -t dummy_bot .

## Create container

docker run -d --name commercial_agent -p 80:80 dummy_bot

## Run locally

Project configuration locally with a virtual environment

> python -m venv .venv
> pip install -r requirements.txt

### Start local server

> fastapi dev app/main.py