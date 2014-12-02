#!/usr/bin/env python
import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import CellMarks

def init(ip=None,browser=None):
    cellmark = dbmobile_model.CellMarks()
    cellmark.source_ip = None    
    #session.add(cellmark)
    #session.commit()
    return cellmark

def add( cellmark ):
    #image = dbmobile_model.Images()
    #image.description = description
    session.add(cellmark)
    session.commit()

def first():
    cellmark =  session.query(CellMarks).first()

def last():
    return session.query(CellMarks).last()

def remove(value):
     session.query(CellMarks).filter_by(id=value).delete()

def get(value):
    return session.query(CellMarks).filter_by(id=value).first()

def getall():
    return  session.query(CellMarks).all()
