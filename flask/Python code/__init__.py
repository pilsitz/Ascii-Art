"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.debug = True
import flaskv4.views

