from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='record.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

app=Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import routes



with app.app_context(): 
    db.create_all()