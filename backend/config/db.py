from pymongo import MongoClient
from decouple import config

client = MongoClient(config("URL"))

database = client.TodoList
collection = database.todo
