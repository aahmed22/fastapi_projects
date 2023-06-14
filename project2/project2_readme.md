# Data Validation and Status Codes

In this project, the focus will be on showcasing data validations and status codes in our FastAPI app. 

Here is a list of our API endpoints for this project:
* (GET) /items
* (GET) /items/{item_id}
* (DELETE) /items/{item_id}
* (GET) /items/
* (GET) /items/year_released/
* (POST) /create-item
* (PUT) /update_item

![HTTP Endpoints Project2]('https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project2/overview_api_endpoints_project2.PNG')


In our project example we are going to have a list called **"STORE"** which will hold a list of ***"StoreItem objects"***. 

Here's our list:
```python
STORE = [
    StoreItem(1, 'Standing Computer Desk', 499.99, 'A mobile standing computer desk with wheels', 5, 2020),
    StoreItem(2, 'Black L-Shaped Sofa', 799.99, 'Big L-Shaped Sofa with cup holders built-in', 4, 2021),
    StoreItem(3, 'Floor Living Room Lamp', 99.99, 'Tall living room lamp', 3, 2022),
    StoreItem(4, 'Dining Room Table', 399.99, 'A simple dining room table', 2, 2015),
    StoreItem(5, 'Home Office Desk Chair', 299.99, 'A black office desk chair for home', 5, 2020)
]
```

Below is our class **StoreItem** and we have included a constructor to initialize the object. 
```python
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

```


## Pydantics and Data Validation
Pydantics is a library that is used for data validation and how to handle data coming to our FastAPI app. 

```python
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
```