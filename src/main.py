from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class Food(BaseModel):
    name: str
    ingredients: List[str] = []


@app.post("/food_summary")
async def prepare_food(food: Food):
    return {"message": f"Preparing {food.name}"}


@app.post("/food_delivery")
async def get_food_delivery(food: Food, delivery: bool = False):
    return {"message": f"Preparing {food.name}", "delivery": f"{delivery}"}


@app.post("/food_ingredients")
async def get_food_ingredients(food: Food):
    all_ingredients = []
    for i in food.ingredients:
        all_ingredients.append(i.lower())
    return {"message": f"Preparing {food.name}", "ingredients": f"{all_ingredients}"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    return {"Info": "This is a test project to see how to create API Endpoints"}


@app.get("/predict")
async def predict():
    return {"prediction": "Test"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main.app", host="127.0.0.1", port=8000)
