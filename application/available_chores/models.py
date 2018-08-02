from application import db

class AvailableChore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    household = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    choretype= db.Column(db.Integer, nullable= False)    
    def __init__(self, household):
        self.household = household
        self.points = 10
        self.choretype= "Imurointi"
        
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

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(32), nullable=False)
    def __init__(self, name):
        self.name= name
        self.points=0    
    