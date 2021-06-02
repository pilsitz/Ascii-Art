"""
Routes and views for the flask application.
"""

import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, send_file
from flaskv4 import app
from .backend import *
#
#app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER + "/static/images"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
#ICI PATH A MODIFIER
path_final = "C:/Users/Navarro/Desktop/flaskv4/flaskv4/static/images"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        file.filename = "new.jpg"
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        usk2(f)

        return redirect(url_for('show'))
    return render_template('upload.html')

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return render_template('show.html')

@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response