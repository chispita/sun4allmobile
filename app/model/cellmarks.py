#!/usr/bin/python

import json
from app.core import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy  import Integer,String, DateTime,Float

class CellMarks(db.Model):
    __tablename__ = 'cellmarks'
    id = Column(Integer, primary_key = True)
    typeofmarking = Column(db.Integer)
    x = Column(Integer)
    y = Column(Integer)
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    result_id = Column(Integer, ForeignKey('cellresults.id'), nullable=False)

    def __repr__(self):
        return '<CellMarks: %s-%s: typeofmarking:%s x:%s, y:%s>' % (self.id, self.result_id,self.typeofmarking,self.x,self.y)

