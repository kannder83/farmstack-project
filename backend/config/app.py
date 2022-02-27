
from fastapi import FastAPI
from app.routes.todo import todo
from fastapi.middleware.cors import CORSMiddleware


def get_application():

    app = FastAPI(
        title="ToDo APP",
        description="FARM Stack",
        docs_url="/"
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(todo)

    return app


application = get_application()
