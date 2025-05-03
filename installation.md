# Dummy bot

## Create image

```console
docker build -t dummy_bot .
```

## Create container

```console
docker run -d --name commercial_agent -p 80:80 dummy_bot
```

## Run locally

Project configuration locally with a virtual environment

```console
source src/.venv/bin/activate
pip3 install -r src/requirements.txt
```

### Start local server

```console
fastapi dev src/app/server.py
```

## AWS deployment

Requirements:

Create a user for api calls in IAM in aws web console and download credentials to configure aws cli.

### Install AWS CLI

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

After installation you have to set credential, execting the following commands:

```console
aws configure
```

set the secrets:

```console
[default]
aws_access_key_id = 
aws_secret_access_key = 
```

## Install terraform

https://developer.hashicorp.com/terraform/install

Execute the following commands to create the aws resources to deploy the code:

```console
cd infraestructure
terraform init
terraform plan
terraform apply
```
