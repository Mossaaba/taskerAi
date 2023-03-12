import os

import requests
import openai

api_endpoint = "https://api.openai.com/v1/completions"
openai.api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write Hello wolrd",
    "max_tokens": 500,
    "temperature": 0.5
}


response = requests.post(
    api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print("OK")
else:
    print("NOT OK")
