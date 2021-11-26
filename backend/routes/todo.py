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
    try:
        return todosEntity(collection.find())
    except:
        raise HTTPException(status_code=404, detail="No ToDos found.")

@todo.get("/api/todo/{title}")
async def find_post(title:str):
    try:            
        list_posts=[]
        for post in collection.find({"title": title}):
            print(post)
            list_posts.append(post)
        if list_posts!=[]:
            return todosEntity(list_posts)
        raise HTTPException(status_code=404, detail="No ToDo found.")
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")

@todo.get("/api/todo/{word}")
async def find_post_word(word:str):
    try:            
        list_posts=[]
        for post in collection.find({"$text": {"$search": word}}):
            print(post)
            list_posts.append(post)
        if list_posts!=[]:
            return todosEntity(list_posts)
        raise HTTPException(status_code=404, detail="No ToDo found.")
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")

@todo.post("/api/todo")
async def create_todo(todo: Todo):
    try:
        id = collection.insert_one(dict(todo)).inserted_id
        return {"msg": "ok", "data": todoEntity(collection.find_one({"_id": ObjectId(id)}))}
    except:
        raise HTTPException(status_code=404, detail="No ToDo has been created.")

        