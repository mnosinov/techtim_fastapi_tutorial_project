from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    },
    2: {
        "name": "Bread",
        "price": 1.99,
        "brand": "White"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return {
        "Data": inventory[item_id]
    }
