from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text     

class DoneChore(Base):
    userid=db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    choreid =db.Column(db.Integer, db.ForeignKey('chore.id'), nullable=False)
    points= db.Column(db.Integer, nullable=False)
    
    def __init__(self, userid, choreid, points):
        self.userid = userid
        self.choreid= choreid
        self.points=points
        
    @staticmethod
    def user_done_chores():
        stmt = text("SELECT Account.id, Account.name, chore.choretype, "
                    "done_chore.points, done_chore.date_created FROM done_chore "
                    "INNER JOIN Account ON done_chore.userid=Account.id "
                    "INNER JOIN chore ON done_chore.choreid=chore.id "
                    "INNER JOIN household ON account.household= household.id"
                    " WHERE account.household= " + str(current_user.household) +";")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "choretype": row[2], "points": row[3], "date": row[4]})
        return response

