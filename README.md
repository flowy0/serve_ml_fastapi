# Repo to try serving ML models using Fast API




#### Setup Virtual Environment
```
conda create -n fastapi python=3.8
conda activate fastapi
pip install -r requirements.txt
```

#### Run FastAPI
Run the App in your command line
```
uvicorn main:app --reload
```

or 
```
python main.py
```

or
run the script `./run.sh`

<br>

#### Access the web interface
View the API via your browser at 
- http://127.0.0.1:8000/docs
  or 
- http://127.0.0.1:8000/redoc


### Data/Model Preparation

We have prepared a simple Random Forest Model for purposes of serving it via FastAPI.


Here are the steps:
 - Download Data from Kaggle (California Housing)
 - Explored the data
 - Removed some missing values (<1% of the data>)
 - Removed Categorical Variables
 - Prepared a Random Forest Regressor using Sklearn
 - Saved to the model to a pkl file

The scripts below are run in succession:
1. scripts/get_kaggle_data.sh
2. src/clean_data.py
3. prepare_model.py

Notebook:
 - notebooks/explore_data.ipynb

