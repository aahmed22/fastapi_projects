from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class StoreItem:
    id: int
    name: str
    cost: float
    description: str
    rating: int 
    year_release: int 

    def __init__(self, id, name, cost, description, rating, year_release):
        self.id = id
        self.name = name
        self.cost = cost
        self.description = description
        self.rating = rating
        self.year_release = year_release


class ItemRequest(BaseModel):
    id: Optional[int] = Field(name='id is not needed')
    name: str = Field(min_length=3)
    cost: float = Field(gt=0.0)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=1, lt=6)
    year_release: int = Field(gt=1999, lt=2031)

    class Config:
        schema_extra = {
            'example': {
                'name': 'A new item',
                'cost': 12.99,
                'description': 'A new description of store item',
                'rating': 5,
                'year_release': 2023
            }
        }

STORE = [
    StoreItem(1, 'Standing Computer Desk', 499.99, 'A mobile standing computer desk with wheels', 5, 2020),
    StoreItem(2, 'Black L-Shaped Sofa', 799.99, 'Big L-Shaped Sofa with cup holders built-in', 4, 2021),
    StoreItem(3, 'Floor Living Room Lamp', 99.99, 'Tall living room lamp', 3, 2022),
    StoreItem(4, 'Dining Room Table', 399.99, 'A simple dining room table', 2, 2015),
    StoreItem(5, 'Home Office Desk Chair', 299.99, 'A black office desk chair for home', 5, 2020)
]


@app.get("/items", status_code=status.HTTP_200_OK)
async def read_all_items():
    return STORE


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int = Path(gt=0)):
    for item in STORE:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found!')


@app.get("/items/", status_code=status.HTTP_200_OK)
async def read_item_by_rating(item_rating: int = Query(gt=0, lt=6)):
    items_to_return = []
    for item in STORE:
        if item.rating == item_rating:
            items_to_return.append(item)
    return items_to_return


@app.get("/items/year_released/", status_code=status.HTTP_200_OK)
async def read_item_by_year_release(year_release: int = Query(gt=2000, lt=2024)):
    items_based_on_year_release_return = []
    for item in STORE:
        if item.year_release == year_release:
            items_based_on_year_release_return.append(item)
    return items_based_on_year_release_return


@app.post("/create-item", status_code=status.HTTP_201_CREATED)
async def create_item(item_request: ItemRequest):
    new_item = StoreItem(**item_request.dict())
    STORE.append(find_item_id(new_item))

def find_item_id(item: StoreItem):
    item.id = 1 if len(STORE) == 0 else STORE[-1].id + 1
    return item


@app.put("/items/update_item", status_code=status.HTTP_204_NO_CONTENT)
async def update_item(item: ItemRequest):
    item_changed = False
    for i in range(len(STORE)):
        if STORE[i].id == item.id:
            STORE[i] = item 
            item_changed = True
    if not item_changed:
        raise HTTPException(status_code=404, detail='Item not found!')
    

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int = Path(gt=0)):
    item_changed = False
    for i in range(len(STORE)):
        if STORE[i].id == item_id:
            STORE.pop(i)
            item_changed = True
            break
    if not item_changed:
        raise HTTPException(status_code=404, detail='Item not found!')