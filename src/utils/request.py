from typing import ByteString
from urllib.parse import parse_qsl

def convert_byte_string_request_to_dict(body: ByteString) -> str:
    return dict(parse_qsl(body.decode()))