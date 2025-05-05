# Commercial Agent

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
make start-local-server
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


### Install ngrok

We use ngrok to expose the local application to public access and configure our endpoint as a webhook to receive messages from twilio.

Install ngrok with the instructions on the [Official documentation](https://ngrok.com/docs/getting-started/)
After installation run the commands below:

```console
ngrok config add-authtoken YOUR_TOKEN
ngrok http http://127.0.0.1:8000
```

![ngrok terminal](/docs/img/ngrok_terminal.png)
