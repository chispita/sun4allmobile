#!/usr/bin/env python
import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import CellResults

def init(ip=None,browser=None):
    result = dbmobile_model.CellResults()
    result.image_name= None
    result.source_ip = None    
    #session.add(result)
    #session.commit()
    return result

def add( result ):
    #image = dbmobile_model.Images()
    #image.description = description
    
    session.add(result)
    session.commit()

def first():
    result =  session.query(CellResults).first()

def last():
    return session.query(CellResults).last()

def remove(value):
     session.query(CellResults).filter_by(id=value).delete()

def get(value):
    return session.query(CellResults).filter_by(image_name=value).first()

def getall():
    return  session.query(CellResults).all()
