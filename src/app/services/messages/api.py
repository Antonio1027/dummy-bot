import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

def get_response(content: str):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=content,
        to='whatsapp:+5219611103182'
    )
    return message
