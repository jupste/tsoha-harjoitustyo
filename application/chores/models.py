from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text

class AvailableChore(Base):
    __tablename__ = "chore"
    householdid = db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    maxpoints = db.Column(db.Integer, nullable=False)
    choretype= db.Column(db.Integer, db.ForeignKey('choretype.id'), nullable= False)
    message= db.Column(db.String(144), nullable= True)
    type_index=db.Index("type_index", choretype)

    def __init__(self, householdid, points, choretype):
        self.householdid = householdid
        self.points=points
        self.maxpoints=points
        self.choretype=choretype
    @staticmethod
    def list_chores(household):
        res=""
        try:
            stmt = text("SELECT chore.id, chore.points, chore.maxpoints, choretype.name "
                        "FROM chore INNER JOIN choretype ON chore.choretype=choretype.id "
                        " WHERE chore.householdid= " + str(household) +" AND chore.points>0;")
            res = db.engine.execute(stmt)
        except Exception as e:
            return render_template("/error.html", message= e.message)
        response = []
        for row in res:
            response.append({"id":row[0], "points":row[1], "maxpoints": row[2], "choretype": row[3]})
        return response