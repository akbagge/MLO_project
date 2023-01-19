import pytest
import src
from flask import *
from src.api.main import app
import io
from io import StringIO 
from io import BytesIO

def test_upload_noFile():
    tester = app.test_client()
    response = tester.post('/')
    #print(response)
    assert  b'No file' in response.data

def test_good():
    tester = app.test_client()
    with open('tests/data/a11.jpg', 'rb') as img1:
        imgStringIO1 = (BytesIO(img1.read()))

        response = tester.post('/',content_type='multipart/form-data', 
                                    data={'image': (imgStringIO1, 'a11.jpg'),
                                          'files': (imgStringIO1, 'a11.jpg')})
        assert (response.status == "200 OK")

def test_upload_noInput():
    tester = app.test_client()
    with open('tests/data/a11.jpg', 'rb') as img1:
        imgStringIO1 = (BytesIO(img1.read()))

    response = tester.post('/',content_type='multipart/form-data', 
                                    data={'name':'test_item',
                                          'user_id':'1',
                                          'username':'admin',
                                          'image': (imgStringIO1, 'img1.jpg')})
    assert (response.status == "200 OK")


def test_upload_NoFileSelected():
    tester = app.test_client()
    with open('tests/data/a11.jpg', 'rb') as img1:
        imgStringIO1 = (BytesIO(img1.read()))

    response = tester.post('/',content_type='multipart/form-data', 
                                    data={'name':'test_item',
                                          'user_id':'1',
                                          'username':'admin',
                                          'image': (b'', 'img1.jpg')})
    assert (response.status == "200 OK")


def test_upload_get():
    tester = app.test_client()

    response = tester.get('/')
    assert (response.status == "200 OK")




