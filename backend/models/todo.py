from pydantic import BaseModel
from pydantic import Field
from bson.objectid import ObjectId


# class Todo(BaseModel):
#     _id: ObjectId
#     title: str = Field(
#         ...,
#         min_length=1,
#         max_length=100,
#         regex='^[A-Za-z]*$'
#     )
#     description: str = Field(
#         ...,
#         min_length=1,
#         max_length=200
#     )

class Todo(BaseModel):
    _id: ObjectId
    title: str
    description: str
