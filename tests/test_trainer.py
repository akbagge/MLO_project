import tests
import src

from src.models.train_model import *

"python3 src/models/train_model.py --data-dir output --num_classes 5 --img-size 224 -b 50 --epochs 10 --pretrained --experiment timm"
if(os.path.exists("output")):
    splitfolders.ratio("Rice_Image_Dataset", output="output", seed=1337, ratio=(.8, .2), group_prefix=None, move=False)
    os.rename('output/val', 'output/validation')    