from sqlalchemy.engine.url import URL
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
from . import app
import os


DATABASE_URL = os.environ.get(
    'DATABASE_URL', '') or "postgresql://yaqfsxtfrvpnqw:0d59a3e541dd796adf2ef1fbf31c2c0d84c46c59d966db0990cd026ca01894d6@ec2-184-72-235-80.compute-1.amazonaws.com:5432/dbftqqmnch7b9g"

# Next line is added to avoid the Sqlalchemy error. Heroku stillhas postgres as part of the URL,
#  it should be postgresql

DATABASE_URL = "postgresql://yaqfsxtfrvpnqw:0d59a3e541dd796adf2ef1fbf31c2c0d84c46c59d966db0990cd026ca01894d6@ec2-184-72-235-80.compute-1.amazonaws.com:5432/dbftqqmnch7b9g"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


def getApiInfo():
    print("entering getapiinfo")
    engine = db.engine
    print(DATABASE_URL)
    # engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    data = pd.read_sql("SELECT * FROM apikey where id = 1", conn)
    # print(data)
    key = data['api_key'][0]
    baseurl = data['base_url'][0]
    print(key)
    # key = "rcKKCFQ6gSUy4R_8fQ2y"
    # baseurl = "https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01"
    return key, baseurl
