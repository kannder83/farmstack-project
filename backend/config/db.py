from pymongo import MongoClient
from .config import settings

DB_URL = f'mongodb+srv://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}?retryWrites=true&w=majority'

client = MongoClient(DB_URL)

database = client.TodoList
collection = database.todo
