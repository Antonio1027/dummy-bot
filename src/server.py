from fastapi import FastAPI, Request
from src.domain.chat.message_processor import message_processor
from src.utils.request import convert_byte_string_request_to_dict

app = FastAPI()

@app.post("/commercial-assistant")
async def reply_message(request: Request):
    body = await request.body()
    data = convert_byte_string_request_to_dict(body)
    return message_processor(data.get("Body"), data.get("From"), data.get("To"))