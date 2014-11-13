#!/usr/bin/env python
import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import Images

def init(ip=None,browser=None):
    image = dbmobile_model.Points()
    image.source_ip = None    
    session.add(image)
    session.commit()
    return image

def add( point ):
    #image = dbmobile_model.Images()
    #image.description = description
    session.add(point)
    session.commit()

def first():
    point =  session.query(Points).first()

def last():
    return session.query(Points).last()

def remove(value):
     session.query(Points).filter_by(id=value).delete()

def get(value):
    return session.query(Points).filter_by(id=value).first()

def getall():
    return  session.query(Points).all()
