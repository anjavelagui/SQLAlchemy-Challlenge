from _typeshed import NoneType
import numpy as np
import datetime as dt
from datetime import timedelta
import pandas as pd
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

# Setting up Database
engine = create_engine("sqlite://Resources/hawaii.sqlite")
dbase = automap_base()
dbase.prepare(engine, reflect=True)

# Saving references to tables
measurementtbl = dbase.classes.measurement
stationtbl = dbase.classes.station

#creating session from Py to DB
session = Session(engine)

# Setting up Flask
app = Flask(__name__)
@app.route('/')
def Home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precepitation<br/>"
        f"/api/v1.0/stationtbl<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )
@app.route("api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    recent_date =session.query(measurementtbl.date).order_by(measurementtbl.date.desc()).first().date
    yearago = (dt.datetime.strptime(recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    session.query(stationtbl.id).count()
    actv_stations = session.query(measurementtbl.station, func.count(measurementtbl.station)).group_by(measurementtbl.station).order_by(func.count(measurementtbl.station).desc()).all()
    session.query(func.min(measurementtbl.tobs), func.max(measurementtbl.tobs), func.avg(measurementtbl.tobs)).filter(measurementtbl.station == ma_station).all()
    return jsonify (top_station_year_obsv)
@app.route("/appi/v1.0/temp/<start>")
@app.route("/appi/v1.0/temp/<start>/<end>")
def start(start =none, end = NoneType):
    session = Session(engine)
    session.query(func.min(measurementtbl.tobs), func.max(measurementtbl.tobs), func.avg(measurementtbl.tobs)).filter(measurementtbl.station == ma_station).all()
    if not end:
