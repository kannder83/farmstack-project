def todoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"]
    }


def todosEntity(entity) -> list:
    return [todoEntity(item) for item in entity]
