import os
from dotenv import load_dotenv
import openai
from getpass import getpass


ENV_path = os.path.join(".secrets", ".env")
load_dotenv(dotenv_path=ENV_path)
if os.getenv('CHAT_GPT_API_KEY') is None:
    API_KEY = getpass("Input your API key: ")
    openai.api_key = API_KEY
    print("API key received: " + "*" * len(API_KEY))

    with open(ENV_path, "a") as file:
        file.write(f"CHAT_GPT_API_KEY={API_KEY}\n")
else:
    openai.api_key = os.getenv('CHAT_GPT_API_KEY')

def get_response_from_ChatGPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",

        messages=[
            {"role": "system", "content": "You are an expert YouTuber who knows the ins and outs about perfect titles and descriptions. You are to advice me by giving me the best titles and descriptions based on the given idea or starting point."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content