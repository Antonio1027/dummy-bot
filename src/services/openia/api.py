import json
from openai import OpenAI
from src.services.aws.secret_manager import get_secret
from src.database.repositories.car_respository import CarRepository

client = OpenAI(api_key=get_secret('OPENAI_API_KEY'))

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content

# def get_tools():
#     return [{
#         "type": "function",
#         "function": {
#             "name": "get_cars_with_detail",
#             "description": "Use this function to get more information about a car",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "version": {"type": "string", "description": "This is the version of a car that belongs to a brand"},
#                     "year": {"type": "string", "description": "Car manufactured year"}
#                 },
#                 "required": ["version", "year"],
#                 "additionalProperties": False
#             }
#         }
#     }]


