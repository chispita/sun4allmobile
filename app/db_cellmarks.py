#!/usr/bin/env python
from core import db
from model import CellMarks

def init(ip=None,browser=None):
    result=CellMarks()
    result.source_ip=ip
    result.browser=browser
    return result

def add(cellmark):
    db.session.add(cellmark)
    db.session.commit()

def first():
    cellmark=CellMarks.query.first()

def last():
    return CellMarks.query.last()

def remove(value):
     CellMarks.query.filter_by(id=value).delete()

def get(value):
    return CellMarks.query.filter_by(id=value).first()

def getall():
    return CellMarks.query.all()
