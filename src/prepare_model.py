import pandas as pd
import logging
import utils
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
import joblib

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
logger.info(X.info())

logger.info(X.describe())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# def get_DT_mae(max_leaf_nodes, X_train, X_test, y_train, y_test):
#     model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
#     model.fit(X_train, y_train)
#     preds_val = model.predict(X_test)
#     mae = mean_absolute_error(y_test, preds_val)
#     return(mae)

# best_mae =100000
# for max_leaf_nodes in [5, 50, 250, 350, 500, 750, 1000, 5000]:
#     my_mae = get_DT_mae(max_leaf_nodes, X_train, X_test, y_train, y_test)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))    
#     # get smallest error
#     if my_mae < best_mae:
#         best_mae=my_mae
#         best_tree_size=max_leaf_nodes

# logger.info(f"Best Tree Size: {best_tree_size}")

# # logger.info()
# logger.info("Retrain Model:")
# DT_model=DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=42)
# DT_model.fit(X_train, y_train)
# predictions = DT_model.predict(X_test)
# # logger.info(predictions)

# MAE = mean_absolute_error(y_test, predictions)
# logger.info(f"MAE:{MAE}")

# logger.info("Save the DT model")
# # Save to file in the current working directory
# utils.create_dir(file_path=DT_MODEL_OUTPUT)
# with open(DT_MODEL_OUTPUT, 'wb') as file:
#     pickle.dump(DT_model, file)
# logger.info(f"Model saved to {DT_MODEL_OUTPUT}")


logger.info("Try Random Forest Regressor")
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

logger.info(rf_model.estimators_)

predictions = rf_model.predict(X_test)
# logger.info(predictions)



MAE = mean_absolute_error(y_test, predictions)
logger.info(f"MAE for Random Forest:{MAE}")

def get_RF_mae(max_leaf_nodes, X_train, X_test, y_train, y_test):
    model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(X_train, y_train)
    preds_val = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds_val)
    return(mae)

best_mae =100000
for max_leaf_nodes in [5, 50, 250, 350, 500, 750, 1000, 5000]:
    my_mae = get_RF_mae(max_leaf_nodes, X_train, X_test, y_train, y_test)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))    
    # get smallest error
    if my_mae < best_mae:
        best_mae=my_mae
        best_tree_size=max_leaf_nodes

logger.info(f"Best Tree Size: {best_tree_size}")



rf_model2 = RandomForestRegressor(max_leaf_nodes=best_tree_size, random_state=42)
rf_model2.fit(X_train, y_train)

utils.create_dir(file_path=RF_MODEL_OUTPUT)
with open(RF_MODEL_OUTPUT, 'wb') as file:
    pickle.dump(rf_model, file)
logger.info(f"Model saved to {RF_MODEL_OUTPUT}")

# compress model
joblib.dump(rf_model,  'models/rf_model_compress.pkl',compress=3)
logger.info(f"Compresssed Model saved to rf_model_compress.pkl")


# test model performance
y_pred_test = rf_model.predict(X_test)




print(f'Model test with criterion MAE: {mean_absolute_error(y_test, y_pred_test):0.2f}')


# if __name__ == "__main__":
#     pass