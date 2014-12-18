#!/usr/bin/env python
from core import db
from model.cellmarks import CellMarks

def init(ip=None,browser=None):
    cellmark=db.CellMarks()
    cellmark.source_ip=None    
    return cellmark

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
