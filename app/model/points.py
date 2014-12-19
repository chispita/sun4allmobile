#!/usr/bin/python

import json
from app.core import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy  import Integer,String, DateTime,Float

class Points(db.Model):
    __tablename__ = 'points'
    id = Column(Integer, primary_key = True)
    x = Column(Float(precision=2), default=0)
    y = Column(Float(precision=2), default=0)
    width = Column(Float(precision=2), default=0)
    browser = Column(String(100), default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    images_id = Column(Integer, ForeignKey('images.id'), nullable=False)

    def __repr__(self):
         return '<Points: %s-%s: x:%s, y:%s, width:%s>' % (self.id, self.images_id,self.x,self.y,self.width)
