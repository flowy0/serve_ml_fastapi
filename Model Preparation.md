We have prepared a simple Random Forest Model for purposes of serving it via FastAPI.


Here are the steps:
 - Download Data from Kaggle (California Housing)
 - Explored the data
 - Removed some missing values (<1% of the data>)
 - Removed Categorical Variables
 - Prepared a Random Forest Regressor using Sklearn
 - Saved to the model to a pkl file


The scripts below are run in succesion:
1. scripts/get_kaggle_data.sh
2. src/clean_data.py
3. prepare_model.py

Notebook:
 - notebooks/explore_data.ipynb