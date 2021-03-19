
import os
import pandas as pd
import logging
import utils

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

DATASET_LINK='https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv'
# DATA_RAW='data/raw/housing.csv'
DATASET_RAW='data/raw/housing.csv'
nested_dir, filename = os.path.split(DATASET_RAW)





#download the file to our specified directory
utils.create_dir(file_path=DATASET_RAW)
if not os.path.exists(DATASET_RAW):
    os.system(f"curl {DATASET_LINK} --output {DATASET_RAW}")
    logger.info(f"download files to {DATASET_RAW}")
else:
    logger.info(f"{DATASET_RAW} already downloaded")

logger.info(f"reading file {DATASET_RAW}")
df = pd.read_csv(DATASET_RAW)
logger.info(df.info())
logger.info(df.head())

