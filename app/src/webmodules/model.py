'''
models - database models for application
===========================================
'''

# standard
from datetime import datetime
from collections import OrderedDict

# pypi
from flask import g
from flask_sqlalchemy import SQLAlchemy

# home grown
# need to use a single SQLAlchemy() instance, so pull from loutilities.user.model
# from loutilities.user.model import db, LocalUserMixin, ManageLocalTables, EMAIL_LEN
# from loutilities.user.tablefiles import FilesMixin
db = SQLAlchemy()

# set up database - SQLAlchemy() must be done after app.config SQLALCHEMY_* assignments
Table = db.Table
Index = db.Index
Column = db.Column
Integer = db.Integer
Float = db.Float
Boolean = db.Boolean
String = db.String
Text = db.Text
Date = db.Date
Time = db.Time
DateTime = db.DateTime
Sequence = db.Sequence
Enum = db.Enum
Interval = db.Interval
UniqueConstraint = db.UniqueConstraint
ForeignKey = db.ForeignKey
relationship = db.relationship
backref = db.backref
object_mapper = db.object_mapper
Base = db.Model

class Blog(Base):
    __tablename__ = 'blog'
    id      = Column(Integer(), primary_key=True)
    title   = Column(Text)
    