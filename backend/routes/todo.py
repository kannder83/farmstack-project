from config.db import collection
from models.todo import Todo

from fastapi import APIRouter, HTTPException
from fastapi import Body, Query, Path
from schemas.todo import todoEntity, todosEntity
from bson.objectid import ObjectId


todo = APIRouter()



@todo.get("/api/todo")
async def find_all_todos():
    try:
        return todosEntity(collection.find())
    except:
        raise HTTPException(status_code=404, detail="No ToDos found.")


@todo.post("/api/todo")
async def create_todo(todo: Todo):
    try:
        id = collection.insert_one(dict(todo)).inserted_id
        return {"msg": "ok", "data": todoEntity(collection.find_one({"_id": ObjectId(id)}))}
    except:
        raise HTTPException(status_code=404, detail="No ToDo has been created.")


@todo.get("/api/todo/title/{title}")
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


@todo.put("/api/todo/{id}")
async def update_post(id:str,todo:Todo):
    try:
        todoEntity(collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)}))            
        return todoEntity(collection.find_one({"_id": ObjectId(id)}))
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")


@todo.delete("/api/todo/{id}")
async def delete_post(id:str):
    try:
        todoEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))            
        return {"msg":"ok","data":f'Post ID:{id} has been removed.'}
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")