from fastapi import FastAPI 
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World" }

@app.get("/info")
async def info():
    return {"Info": "placeholder" }    

@app.get("/predict")
async def predict():
    return {"prediction": "Test" }    



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 8000)