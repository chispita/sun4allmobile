#!/usr/bin/env python
from core import db
from model.cellresults import CellResults

def init(ip=None,browser=None):
    result=CellResults()
    result.image_name=None
    result.source_ip=None    
    return result

def add( result ):
    db.session.add(result)
    db.session.commit()

def first():
    result= CellResults.query.first()

def last():
    return CellResults.query.last()

def remove(value):
     CellResults.query.filter_by(id=value).delete()

def get(value):
    return CellResults.query.filter_by(image_name=value).first()

def getall():
    return CellResults.query.all()
