#!/usr/bin/python

#from sqlalchemy.ext.declarative import declarative_base
#from flask.ext.jsontools import JsonSerializableBase
#from sqlalchemy import orm
#import datetime
#from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
#from sqlalchemy.types import Integer,Unicode,TIMESTAMP,Float
#from sqlalchemy.schema import MetaData, Sequence
#from sqlalchemy.orm import relationship

import json
from app.core import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy  import Integer,String, DateTime,Float

class CellResults(db.Model):
    __tablename__ = 'cellresults'
    id = Column(Integer, primary_key = True)
    image_name = Column(String, nullable=False)
    browser = Column(String, default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    cellmarks = relationship('CellMarks', cascade='all, delete, delete-orphan', backref='cellresults')

    def __repr__(self):
        return '<Cell Result: %s-%s>' % (self.id, self.image_name)

    def to_json(self):
        result = { 
                'id'            : self.id,
                'image_name'      : self.image_name,
                'browser'       : self.browser,
                'source_ip'     : self.source_ip,
                'created'       : self.created,
                'deleted'       : self.deleted
                }
        
        
        if self.cellmarks:
            result['cellmarks']=[]
            for mark in self.cellmarks:
                result['cellmarks'].append({ 'typeofmarking': mark.typeofmarking, 'x':mark.x, 'y':mark.y})

        return result
    
    def from_json(self,source):

        if 'id' in source:
            self.id = source['id']
        if 'image_name' in source:
            self.image_name = source['image_name']
        if 'deleted' in source:
            self.deleted = source['deleted']
