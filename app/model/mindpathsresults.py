#!/usr/bin/python

import json
from app.core import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy  import Integer,String, DateTime,Float

class MindPathsResults(db.Model):
    __tablename__ = 'mindpathsresults'
    id = Column(Integer, primary_key = True)
    pair_id = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    words = Column(String, nullable=False)
    ids = Column(String, nullable=False)
    browser = Column(String, default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)

    def __repr__(self):
        return '<Mind Paths Result: %s-%s-%s>' % (self.id, self.pair_id, self.words)

    def to_json(self):
        result = { 
                'id'            : self.id,
                'pair_id'       : self.pair_id,
                'length'        : self.length,
                'words'         : self.words,
                'ids'           : self.ids,
                'browser'       : self.browser,
                'source_ip'     : self.source_ip,
                'created'       : self.created,
                'deleted'       : self.deleted
                }
        
        return result

    def from_json(self,source):

        if 'id' in source:
            self.id = source['id']
        if 'pair_id' in source:
            self.pair_id = source['pair_id']
        if 'length' in source:
            self.length = source['length']
        if 'words' in source:
            self.words = json.dumps(source['words'])
        if 'ids' in source:
            self.ids = json.dumps(source['ids'])
        if 'deleted' in source:
            self.deleted = source['deleted']
