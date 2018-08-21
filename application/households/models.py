from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.donechores.models import DoneChore 
from application.weeklychore.models import WeeklyChore

class Household(Base):
    name= db.Column(db.String(144), nullable=False)
    chores= db.relationship('AvailableChore', backref='available', lazy='dynamic')
    weekly_chores= db.relationship('WeeklyChore', backref= 'weekly', lazy= 'dynamic')
    
    def __init__(self, name):
        self.name=name
    
