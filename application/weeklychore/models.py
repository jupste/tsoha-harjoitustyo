from application import app, db
from application.models import Base

class WeeklyChore(Base):
    choretype = db.Column(db.String(144), nullable=False)
    householdid= db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    interval= db.Column(db.Integer, nullable=False)
    points= db.Column(db.Integer, nullable=False)

    def __init__(self, choretype, householdid, interval, points):
        self.choretype=choretype
        self.householdid=householdid
        self.interval=interval
        self.points=points