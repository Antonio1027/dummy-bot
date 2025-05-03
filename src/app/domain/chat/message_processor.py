from src.app.services.messages.api import get_response
from src.app.services.openia.api import get_completion_from_messages

def message_processor(query: str):
    messages = [
        {"role": "system", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": query,
        },
    ]
    content = get_completion_from_messages(messages)
    get_response(content)
    return {
        "message": str(content)
    }