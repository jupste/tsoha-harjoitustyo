from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.donechores.models import DoneChore 
import datetime
from datetime import timedelta
from pytz import timezone
class User(Base):

    __tablename__ = "account"
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    points= db.Column(db.Integer, nullable=False)
    household= db.Column(db.Integer, db.ForeignKey('household.id'),nullable=False)
    nameIndex= db.Index("name_index", name)

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
    
    def roles(self):
        if self.id==1:
            return ["Boss"]
        return ["Peon"]
    
    @staticmethod
    def find_lazy_users():
        time= datetime.datetime.now(timezone('Europe/Helsinki'))- timedelta(days=7)
        stmt = text("SELECT Account.id, Account.name, Household.name FROM Account "
                    "INNER JOIN Household ON Account.household=Household.id "
                    " WHERE Account.id NOT IN (SELECT userid FROM done_chore WHERE done_chore.date_created > '"+ str(time) + "')")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "household": row[2]})
        return response
