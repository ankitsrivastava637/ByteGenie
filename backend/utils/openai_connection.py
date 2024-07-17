import openai
from config.index import OPENAI_KEY

openai.api_key = OPENAI_KEY

def connect_open_ai():
    return openai
