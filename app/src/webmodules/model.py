'''
models - database models for application
===========================================
'''

# standard
from datetime import datetime
from collections import OrderedDict

# pypi
from flask import g

# home grown
# need to use a single SQLAlchemy() instance, so pull from loutilities.user.model
from loutilities.user.model import db, LocalUserMixin, ManageLocalTables
# from loutilities.user.tablefiles import FilesMixin

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

# *** last bit for users/interest
# copied by update_local_tables
class LocalUser(LocalUserMixin, Base):
    __tablename__ = 'localuser'
    id                  = Column(Integer(), primary_key=True)
    interest_id         = Column(Integer, ForeignKey('localinterest.id'))
    interest            = relationship('LocalInterest', backref=backref('users'))
    userpositions       = relationship('UserPosition', back_populates='user')
    version_id          = Column(Integer, nullable=False, default=1)
    __mapper_args__ = {
        'version_id_col' : version_id
    }

# note update_local_tables only copies Interests for current application (g.loutility)
class LocalInterest(Base):
    __tablename__ = 'localinterest'
    id                  = Column(Integer(), primary_key=True)
    interest_id         = Column(Integer)

    version_id          = Column(Integer, nullable=False, default=1)
    __mapper_args__ = {
        'version_id_col' : version_id
    }

# supporting functions
def update_local_tables():
    '''
    keep LocalUser table consistent with external db User table
    '''
    # appname needs to match Application.application
    localtables = ManageLocalTables(db, 'members', LocalUser, LocalInterest, hasuserinterest=True)
    localtables.update()

