from application import db
from application.models import Base

class AvailableChore(Base):
    __tablename__ = "chore"
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
        
class DoneChore(Base):
    userid=db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    choreid =db.Column(db.Integer, db.ForeignKey('chore.id'), nullable=False)
    points= db.Column(db.Integer, nullable=False)
    
    def __init__(self, userid, choreid, points):
        self.userid = userid
        self.choreid= choreid
        self.points=points

