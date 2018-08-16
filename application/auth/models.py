from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.chores.models import DoneChore 
class User(Base):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    points= db.Column(db.Integer, nullable=False)
    household= db.Column(db.Integer, db.ForeignKey('household.id'),nullable=False)

    def __init__(self, name, username, password, household):
        self.name = name
        self.username = username
        self.password = password
        self.points=0
        self.household= household
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    @staticmethod
    def find_lazy_users():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " WHERE Account.id NOT IN (SELECT userid FROM done_chore)")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

class Household(Base):
    name= db.Column(db.String(144), nullable=False)
    chores= db.relationship('AvailableChore', backref='household', lazy='dynamic')
    
    def __init__(self, name):
        self.name=name
    
