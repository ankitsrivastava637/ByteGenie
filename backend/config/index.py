# backend/config/index.py
from langchain import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("DB_SERVER")

db = SQLDatabase.from_uri(connection_string)
