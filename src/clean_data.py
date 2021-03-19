import logging
import utils
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


DATASET_RAW='./data/raw/housing.csv'
DATASET_CLEAN='./data/processed/housing.csv'





df  = pd.read_csv(DATASET_RAW)

logger.info(f"% of missing values: {df['total_bedrooms'].isnull().sum()/len(df):.2%}")
logger.info("before dropping records")
logger.info(df.info())

df.dropna(axis=0,how='any',inplace=True)
logger.info("after dropping records")
logger.info(df.info())


logger.info("drop the field ocean_proximity as a category object")
df.drop(columns=['ocean_proximity'], inplace=True)


utils.create_dir(file_path=DATASET_CLEAN)
df.to_csv(DATASET_CLEAN, index=False)
logger.info(f"Saved file to {DATASET_CLEAN}")