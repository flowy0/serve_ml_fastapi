# Repo to try serving ML models using Fast API

This project aims to do the following
1. Create a simple ML model to try out model serving via FastAPI
2. Test out FastAPI 
3. Deploy the model to Heroku


#### Setup Virtual Environment
```
conda create -n fastapi python=3.8
conda activate fastapi
pip install -r requirements.txt
```

#### Run FastAPI (Locally)
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
 - Download Data from Kaggle (California Housing) - see [Download Data from Kaggle](Download_Data_from_Kaggle.md)
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



### Deployment to Heroku:

Connect your repo to Heroku 


In this case, my app is called `house-prices-app1`

```
heroku git:remote -a house-prices-app1
```

Add the Procfile required

```
web: uvicorn src.main:app --host=0.0.0.0 --port=${PORT:-5000}
```

Add runtime.txt with the content

```
python-3.8.12
```

Add and Commit these 2 files to trigger a deployment to Heroku
```
git add Procfile runtime.txt
git push heroku main  
```


Open the app in the browser
```
heroku open
```

The app is now accessible at https://house-prices-app1.herokuapp.com/docs


References: 
- https://towardsdatascience.com/how-to-build-and-deploy-a-machine-learning-model-with-fastapi-64c505213857
- https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9

### TO-DO:

- Add Dockerfile for re-produciblity
- Add Streamlit Interface for nicer UI




