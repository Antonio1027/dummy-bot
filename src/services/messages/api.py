from twilio.rest import Client
from src.services.aws.secret_manager import get_secret

def get_response(content: str, user_number: str, sender_number: str):
    account_sid = get_secret("TWILIO_ACCOUNT_SID")
    auth_token = get_secret("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            from_=sender_number,
            body=content,
            to=user_number
        )
        return message
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
