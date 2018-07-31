from application import db

class Avchore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    household = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    
    def __init__(self, household):
        self.household = household
        self.points = 10
