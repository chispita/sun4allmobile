#!/usr/bin/env python
import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import MindPathsResults

def init(ip=None,browser=None):
    result = dbmobile_model.MindPathsResults()
    result.pair_id = None
    result.length = None
    result.words = None
    result.ids = None
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
    result =  session.query(MindPathsResults).first()

def last():
    return session.query(MindPathsResults).last()

def remove(value):
     session.query(MindPathsResults).filter_by(id=value).delete()

def get(value):
    return session.query(MindPathsResults).filter_by(pair_id=value).first()

def getall():
    return  session.query(MindPathsResults).all()
