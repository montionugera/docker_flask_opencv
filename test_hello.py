from flask import Flask
from flask_testing import TestCase
import os
from app import app

def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_upload():
    image_path = os.path.join("tests/assets/cat.jpg")

    imageIO = open(image_path, "rb")

    response = app.test_client().post(
        "/upload",
        data={
            "image": imageIO,
        },
        content_type="multipart/form-data"
    )
    assert response.status_code == 200