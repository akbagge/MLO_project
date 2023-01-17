from timm.models.resnet import resnet50
from src.models.predict_model import RiceModel
import timm
from pprint import pprint
from flask import Flask

app = Flask(__name__)

model = RiceModel()
model.eval()

im = "resources/Karacadag/Karacadag (20).jpg"


@app.route("/")
def main_route():
    label, precision = model.predict(im)
    return { 'label': label, 'precision': "{:.2f}%".format(precision)  }
