import os
import hydra
from omegaconf import OmegaConf
from src.models.predict_model import RiceModel
from werkzeug.utils import secure_filename

TESTIMAGEDIR = "tests/data/"

def test_inference():
    #Setup
    model = RiceModel()
    model.eval()

    #Test
    path = "tests/data/a11.jpg"
    label, precision = model.predict(path)
    assert label == "Arborio"

    path = TESTIMAGEDIR + "basmati_5.jpg"
    label, precision = model.predict(path)
    assert label == "Basmati"

    path = TESTIMAGEDIR + "basmati_20.jpg"
    label, precision = model.predict(path)
    assert label == "Basmati"

    path = TESTIMAGEDIR + "Ipsala_11.jpg"
    label, precision = model.predict(path)
    assert label == "Ipsala"


