from application import db

class AvailableChore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    household = db.Column(db.Integer, db.ForeignKey('account.household'), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    maxpoints = db.Column(db.Integer, nullable=False)
    choretype= db.Column(db.Integer, nullable= False)    
    createdBy=db.Column(db.Integer, nullable= True)
    message= db.Column(db.String, nullable= True)
    
    def __init__(self, household, points, choretype):
        self.household = household
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

