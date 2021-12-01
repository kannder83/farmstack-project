from config.db import collection
from models.todo import Todo

from fastapi import APIRouter, HTTPException
from fastapi import status
from schemas.todo import todoEntity, todosEntity
from bson.objectid import ObjectId


todo = APIRouter()


@todo.get(
    path="/api/todo",
    status_code=status.HTTP_200_OK
)
async def find_all_todos():
    try:
        return todosEntity(collection.find())
    except:
        raise HTTPException(status_code=404, detail="No ToDos found.")


@todo.post(
    path="/api/todo",
    response_model=Todo,
    status_code=status.HTTP_201_CREATED
)
async def create_todo(todo: Todo):
    try:
        id = collection.insert_one(dict(todo)).inserted_id
        return todoEntity(collection.find_one({"_id": ObjectId(id)}))
    except:
        raise HTTPException(
            status_code=404, detail="No ToDo has been created.")


@todo.get(
    path="/api/todo/title/{title}",
    status_code=status.HTTP_200_OK
)
async def find_post(title: str):
    try:
        list_posts = []
        for post in collection.find({"title": title}):
            print(post)
            list_posts.append(post)
        if list_posts != []:
            return todosEntity(list_posts)
        raise HTTPException(status_code=404, detail="No ToDo found.")
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")


@todo.put(
    path="/api/todo/{id}",
    response_model=Todo,
    status_code=status.HTTP_200_OK
)
async def update_post(id: str, todo: Todo):
    try:
        todoEntity(collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(todo)}))
        return todoEntity(collection.find_one({"_id": ObjectId(id)}))
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")


@todo.delete(
    path="/api/todo/{id}",
    status_code=status.HTTP_200_OK
)
async def delete_post(id: str):
    try:
        todoEntity(collection.find_one_and_delete({"_id": ObjectId(id)}))
        return {"msg": "ok", "data": f'Post ID:{id} has been removed.'}
    except:
        raise HTTPException(status_code=404, detail="No ToDo found.")
