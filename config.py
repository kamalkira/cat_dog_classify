import os
import toolkit_config
import toolkit_file

configDict = toolkit_config.read_config_general()['config']

DATASET_DIR_1 = configDict['dataset_dir_1']
DATASET_DIR_2 = configDict['dataset_dir_2']

IMG_SIZE = int(configDict['img_size'])

DATA_DMP = 'dataset.npy'
# MODEL_NAME = 'flower_classify.model'
MODEL_NAME = configDict['model_name']

classify_list = ['Cat', 'Dog']

MODEL_DIR = 'models'
MODEL_LOG = 'logs'


def init_folder():
    for folder in [MODEL_DIR, MODEL_LOG]:
        toolkit_file.create_folder(folder)

init_folder()

