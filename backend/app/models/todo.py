from turtle import title
from pydantic import BaseModel
from pydantic import Field
from bson.objectid import ObjectId


class TodoBase(BaseModel):
    _id: ObjectId
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Title ToDo"
    )
    description: str = Field(
        ...,
        min_length=1,
        max_length=200,
        example="Description ToDo"
    )


class Todo(TodoBase):
    pass


class TodoOut(TodoBase):
    id: str = Field(..., example="ID Object")
    title: str = Field(..., example="Title ToDo")
    description: str = Field(..., example="Description ToDo")
