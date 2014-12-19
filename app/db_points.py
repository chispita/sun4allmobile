#!/usr/bin/env python
from core import db
from model.points import Points

def init(ip=None,browser=None):
    point=Points()
    point.source_ip=ip  
    point.browser=browser
    return point

def add(point):
    db.session.add(point)
    db.session.commit()

def first():
    point= Points.query.first()

def last():
    return Points.query.last()

def remove(value):
     Points.query.filter_by(id=value).delete()

def get(value):
    return Points.query.filter_by(id=value).first()

def getall():
    return Points.query.all()
