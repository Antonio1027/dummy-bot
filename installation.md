# Additional configurations

## Docker

### Build Image

Install docker to build the image with the following command:

```console
make build-image
```

### Create container

```console
make setup-container
```

## AWS deployment

This project can be deployed in aws for testing porpuses with terraform, to do that you need to configure AWS cli tool.

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

Terraform is a IaC tool, and we can create cloud resources in many providers.
This project is configured to create the resources in aws.

To create the cloud resources of this project, you have to install terraform locally. Check the documentation on the link below:

https://developer.hashicorp.com/terraform/install

After installation, locate into the root directory of the project and execute the following commands to create the aws resources:

```console
make deploy-service
```