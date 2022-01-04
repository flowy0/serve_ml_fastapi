# test_model.py

import pickle 

import pandas as pd
import logging
import utils
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

DATASET_CLEAN='./data/processed/housing.csv'
DT_MODEL_OUTPUT='models/dtmodel.pkl'
RF_MODEL_OUTPUT='models/rfmodel.pkl'

logger.info("Load cleaned data")
df = pd.read_csv(DATASET_CLEAN)
logger.info(df.info())

y = df['median_house_value']
X = df.drop(columns=['median_house_value'])
# logger.info(X.info())

# logger.info(X.describe())

logger.info(f"{type(X)=}")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"{type(X_test)=}")

print(f"{X_test.iloc[2]=}")


model_file_name='models/rfmodel.pkl'
with open(model_file_name, 'rb') as file:
    model=pickle.load(file)
    

# test_record

# the model takes in a df with the headers
y_pred_test = model.predict(X_test.iloc[:1])
print(f"{y_pred_test=}")

print(X_test.iloc[:1])

print(X_test.iloc[:1].info())

print(X_test.iloc[:1].to_json(orient="table"))


# create a json input that can be accepted 
# longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value
# -122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,452600.0



# input_dataframe = pd.DataFrame.from_dict(input_json)


test_input={
        "longitude":-122.23,
        "latitude": 37.88,
        "housing_median_age": 41.0,
        "total_rooms": 880,
        "total_bedrooms": 129,
        "population": 322,
        "households": 126,
        "median_income": 8565,   
    }

input_df = pd.DataFrame.from_dict([test_input])
print(type(input_df))
print(input_df.info())

results=model.predict(input_df)
print(results)


