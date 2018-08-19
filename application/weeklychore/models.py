from application import app, db

class WeeklyChore(Base):
    choretype = db.Column(db.String(144), nullable=False)
    household= db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    interval= db.Column(db.Integer, nullable=False)
    points= db.Column(db.Integer, nullable=False)

    def __init__(self, choretype, household, interval, points):
        self.choretype=choretype
        self.household=household
        self.interval=interval
        self.points=points