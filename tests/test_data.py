import os
import hydra
from omegaconf import OmegaConf
from src.models.predict_model import RiceModel
from werkzeug.utils import secure_filename

import cv2

TESTIMAGEDIR = "tests/data/"

def test_data():
    
    dir = "Rice_Image_Dataset"

    for root, dirs, files in os.walk(dir):
        for name in files:
            # loading the image
            img = cv2.imread(os.path.join(root, name))
            # fetching the dimensions
            if(".jpg" in name):
                wid = img.shape[1]
                hgt = img.shape[0]
                # displaying the dimensions
                assert wid == 250 and hgt == 250
            

    

