from application import app, db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user
class WeeklyChore(Base):
    choretype = db.Column(db.Integer, db.ForeignKey('choretype.id'), nullable=False)
    householdid= db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    interval= db.Column(db.Integer, nullable=False)
    points= db.Column(db.Integer, nullable=False)
    last_made=db.Column(db.DateTime, nullable=False)

    def __init__(self, choretype, householdid, interval, points, last_made):
        self.choretype=choretype
        self.householdid=householdid
        self.interval=interval
        self.points=points
        self.last_made=last_made

    @staticmethod
    def list_weeklychores():
        res=""
        try:
            stmt = text("SELECT weekly_chore.id, weekly_chore.points, weekly_chore.interval, choretype.name "
                        "FROM weekly_chore INNER JOIN choretype ON weekly_chore.choretype=choretype.id "
                        " WHERE weekly_chore.householdid= " + str(current_user.household) +";")
            res = db.engine.execute(stmt)
        except Exception as e:
            return render_template("/error.html", message= e.message)
        response = []
        for row in res:
            response.append({"id":row[0], "points":row[1], "interval": row[2], "choretype": row[3]})
        return response