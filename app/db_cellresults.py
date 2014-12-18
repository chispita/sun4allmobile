#!/usr/bin/env python
from core import db
from model import CellResults

def init(ip=None,browser=None):
    result=CellResults()
    result.source_ip=ip
    result.browser=browser
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
