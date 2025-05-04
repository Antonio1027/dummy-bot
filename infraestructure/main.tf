terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 4.16"
        }
    }
}

provider "aws" {
    region = "us-east-2"
}

variable "OPENAI_API_KEY" {
    type = string
}

variable "TWILIO_ACCOUNT_SID" {
    type = string
}

variable "TWILIO_AUTH_TOKEN" {
    type = string
}
