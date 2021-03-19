import os 

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

def create_dir(file_path):
    '''
    Create directory if the file path does not exist
    args: file_path
    '''

    nested_dir, filename = os.path.split(file_path)
    if not os.path.exists(nested_dir):
        os.mkdir(nested_dir)
        logger.info(f"dir {nested_dir} created")