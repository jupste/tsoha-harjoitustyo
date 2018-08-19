from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.donechores.models import DoneChore 

class Household(Base):
    name= db.Column(db.String(144), nullable=False)
    chores= db.relationship('AvailableChore', backref='household', lazy='dynamic')
    
    def __init__(self, name):
        self.name=name
    
