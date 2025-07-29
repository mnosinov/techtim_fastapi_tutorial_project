from fastapi import FastAPI, Path

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
def get_item(item_id: int = Path(
    ..., description="The ID of the item you'd like to view", gt=0, lt=2)
):
    return {
        "Data": inventory[item_id]
    }


@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

