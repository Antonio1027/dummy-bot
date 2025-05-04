# Commertial Agent

This project create a bot that simulate a commertial agent. The agent is based on LLMs from openIA to create chat completions with the model gpt-3.5-turbo

## Run locally

Project configuration locally with a virtual environment

Requirements:

- python 3.9+
- pip

Download or clone the repository into your projects directory, access to the root path directory of the project and execute the following commands:

```console
make setup-local
```

### Start local server

```console
fastapi dev app/server.py
```

### Environment variable

Create a .env file in the root directory of the project and set the following variables:

```console
OPENAI_API_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
```

The application requires those keys of external API calls:

- OpenIA API 
- Twilio
