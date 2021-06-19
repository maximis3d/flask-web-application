#This file makes the website a python package
from flask import Flask

def create_app():
    app = Flask(__name__) #creates the flask application
    app.config['SECRET_KEY'] = 'bfibfibdidbivisfsodisdv;ifpiwvpddv' #encrypts all data
    return app # returns the app from the function
