from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.donechores.models import DoneChore 
from application.weeklychore.models import WeeklyChore
from flask_login import current_user
class Household(Base):
    name= db.Column(db.String(144), nullable=False)
    chores= db.relationship('AvailableChore', backref='available', lazy=True)
    weekly_chores= db.relationship('WeeklyChore', backref= 'weekly', lazy= True)
    
    def __init__(self, name):
        self.name=name
    
    @staticmethod
    def top_dog():
        stmt = text("SELECT MAX(sum), id, name FROM (SELECT Account.id AS id, Account.name AS name, SUM(done_chore.points) AS sum "
                    "FROM done_chore "
                    "INNER JOIN Account ON done_chore.userid=Account.id "
                    "INNER JOIN household ON account.household= household.id "
                    " WHERE account.household= " + str(current_user.household) +" GROUP BY userid) AS topdog;")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[1], "name":row[2],  "sum": row[0]})
        return response


