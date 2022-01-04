from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import uvicorn
import pickle
import pandas as pd
from pydantic import BaseModel
import joblib 

class data_input(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: int


app = FastAPI()


# load model 
model_file_name='models/rf_model_compress.pkl'
model = joblib.load(model_file_name)

    
def get_pred():
    pass


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    return {"Info": "This is a test project to see how to create API Endpoints"}


@app.post("/predict")
async def single_predict(input: data_input):
    
    # sample input:
#     longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income
# -122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252
        
    # print(input_dict)
    # print(type(input_dict))
    
    print(f"{type(input)=}, {input=}")
    
    # print(f"{type(input_dict)=}, {input_dict=}")
    
    input_df = pd.DataFrame.from_dict([dict(input)])
    print(f"{type(input_df)=}, {input_df=}")
    print(input_df.info())
    
    results=model.predict(input_df)
    print(f"{type(results)=}, {results}")

    results_conv=results[0].astype(float)
    print(f"{type(results_conv)=}, {results_conv}")
    
    return {"prediction": results_conv}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("src.main.app", host="127.0.0.1", port=8000)
