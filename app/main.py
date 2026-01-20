from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


class Item(BaseModel):
    item_id: int
    q: str | None = None


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q: str | None = None) -> Item:
    return Item(item_id=item_id, q=q)
