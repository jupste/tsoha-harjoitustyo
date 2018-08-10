from application import db

class AvailableChore(db.Model):
    __tablename__ = "chore"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    householdid = db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    maxpoints = db.Column(db.Integer, nullable=False)
    choretype= db.Column(db.String(144), nullable= False)
    message= db.Column(db.String, nullable= True)
    
    def __init__(self, householdid, points, choretype):
        self.householdid = householdid
        self.points=points
        self.maxpoints=points
        self.choretype=choretype
        
class DoneChore(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Integer, nullable=False)
    choreid =db.Column(db.Integer, nullable=False)
    points= db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, userid, choreid, points):
        self.userid = userid
        self.choreid= choreid
        self.points=points

