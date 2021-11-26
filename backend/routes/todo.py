from config.db import collection
from models.todo import Todo

from fastapi import APIRouter, HTTPException
from fastapi import Body, Query, Path
from schemas.todo import todoEntity, todosEntity
from bson.objectid import ObjectId


todo = APIRouter()


@todo.get("/")
async def read_root():
    return {"msg": "OK", "data": "This work fine!"}


@todo.get("/api/todo")
async def find_all_todos():
    return todosEntity(collection.find())


@todo.post("/api/todo")
def create_todo(todo: Todo):
    id = collection.insert_one(dict(todo)).inserted_id
    return {"msg": "ok", "data": todoEntity(collection.find_one({"_id": ObjectId(id)}))}
