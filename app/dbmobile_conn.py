#!/usr/bin/python
import dbmobile_model

from core import app
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dbmobile_model import Base, Images, Points


engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), echo=True)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(autoflush=True, bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
session = DBSession()


