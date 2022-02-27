from config.db import collection
from app.models.todo import Todo
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import status
from app.schemas.todo import todoEntity, todosEntity
from app.models.todo import TodoOut
from bson.objectid import ObjectId


todo = APIRouter()


@todo.get(
    path="/api/todo",
    status_code=status.HTTP_200_OK,
    tags=["ToDo"],
    summary="Returns all ToDos created in the app.",
    response_model=List[TodoOut]
)
def find_all_todos():
    """
    **Find all ToDos**

    Returns all the ToDo created in the app.

    **Parameters**: None

    Return a list with a ToDo Model with Id, title and description. 
    """
    try:
        return todosEntity(collection.find())
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDos found.")


@todo.post(
    path="/api/todo",
    response_model=Todo,
    status_code=status.HTTP_201_CREATED,
    tags=["ToDo"],
    summary="Create a ToDo"
)
def create_todo(todo: Todo):
    """
    **Create a ToDo**

    Use for create a ToDo in the app.

    **Parameters:**
        - todo:Todo -> A Todo model with title and description.

    Return a specific ToDo Model with title and description. 
    """
    try:
        id = collection.insert_one(dict(todo)).inserted_id
        return todoEntity(collection.find_one({"_id": ObjectId(id)}))
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDo has been created.")


@todo.get(
    path="/api/todo/title/{title}",
    status_code=status.HTTP_200_OK,
    tags=["ToDo"],
    summary="Returns a specific ToDo"
)
def find_post(title: str):
    """
    **Returns a specific ToDo**

    It is used to return a specific ToDo in the application using the title to search.

    **Parameters:**
        - title:str -> The title of Todo.

    Returns a specific ToDo when searched using the title
    """
    try:
        list_posts = []
        for post in collection.find({"title": title}):
            list_posts.append(post)
        if list_posts != []:
            return todosEntity(list_posts)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDo found.")
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDo found.")


@todo.put(
    path="/api/todo/{id}",
    response_model=Todo,
    status_code=status.HTTP_200_OK,
    tags=["ToDo"],
    summary="Update a ToDo"
)
def update_post(id: str, todo: Todo):
    """
    **Update a specific ToDo**

    It is used to update a specific ToDo in the application using the ID to search.

    **Parameters:**
        - id:str -> The unique ID of each Todo.
        - todo:Todo -> A Todo model with title and description.

    Returns a specific ToDo after updating the data.
    """
    try:
        todoEntity(collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(todo)}))
        return todoEntity(collection.find_one({"_id": ObjectId(id)}))
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDo found.")


@todo.delete(
    path="/api/todo/{id}",
    status_code=status.HTTP_200_OK,
    tags=["ToDo"],
    summary="Delete a specific ToDo"
)
def delete_post(id: str):
    """
    **Delete a specific ToDo**

    It is used to delete a specific ToDo in the application using the ID to search.

    **Parameters:**
        - id:str -> The unique ID of each Todo.

    Returns a message when a ToDo has been successfully deleted.
    """
    try:
        todoEntity(collection.find_one_and_delete({"_id": ObjectId(id)}))
        return {"msg": "ok", "data": f'Post ID:{id} has been removed.'}
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No ToDo found.")
