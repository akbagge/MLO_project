import pytest
import src
from timm.models.resnet import resnet50
import os
from src.models.predict_model import RiceModel
import timm
from pprint import pprint
from flask import Flask, request, flash, render_template
from werkzeug.utils import secure_filename

from src.api import main

@pytest.fixture()
def app():
    main.app.requst

@pytest.fixture()
def client(app):
    return app.test_client()

