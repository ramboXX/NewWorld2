from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import template_rendered
from flask_pymongo import PyMongo
import urllib

app = Flask(__name__)
mongo_uri = 'mongodb+srv://administrator:' + urllib.parse.quote("Adragao@12") + '@cluster0-me8zj.gcp.mongodb.net/test?retryWrites=true&w=majority'
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

from app.controllers import default