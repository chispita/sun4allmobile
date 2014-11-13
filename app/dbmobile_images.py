#!/usr/bin/env python
import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import Images

def init(ip=None,browser=None):
    image = dbmobile_model.Images()
    image.description = None
    image.source_ip = None    
    session.add(image)
    session.commit()
    return image

def add( image ):
    #image = dbmobile_model.Images()
    #image.description = description
    session.add(image)
    session.commit()

def first():
    image =  session.query(Images).first()

def last():
    return session.query(Images).last()

def remove(value):
     session.query(Images).filter_by(id=value).delete()

def get(value):
    return session.query(Images).filter_by(id=value).first()

def getall():
    return  session.query(Images).all()
