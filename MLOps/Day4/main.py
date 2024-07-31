from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "modumodufighting"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "lenet jjange"}

    return {"model_name": model_name, "message": "error"}

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#   return {"Hello": "World"}

# @app.get("/home") # include_in_schema=False
# def health_check_handler():
#     return {"asd": "test"}

# @app.get("/home/{name]*)
# def health_check_handler(name: str):
#     return ("name": name)

# @app.get("/home error/(name)")
# def health_check_handler(name: int):
#     return {"name": name)

# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#   return {"Hello": "GET"}
#
# @app.get("/{item_id}")
# async def read_item(item_id: int, q: Union[str,  None] = None):
#     return {"item_id": item_id, "q": q}
#
# @app.post("/")
# def home_post(msg: str):
#   return {"Hello": "POST", "message": msg}