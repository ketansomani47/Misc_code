from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    item_name: str
    item_price: float
    item_description: str


app = FastAPI()
# global item_list
item_list = []


# Simple API End
@app.get("/")
def read_root():
    return {"Hello": "World"}


# URL PATH
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": "Only URL PATH"}


# URL PATH With Query Params
@app.get("/items/{item_id}/query")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "message": "URL PATH with query string"}


# URL path with body
@app.post("/item")
def post_item(items: Item):
    item_list.append(items)
    return {"id": items.item_id, "name": items.item_name, "price": items.item_price,
            "description": items.item_description, "message": "URL with body"}


# taking item list
@app.get("/item_list")
def get_item_list():
    return {"data": item_list}
