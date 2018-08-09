from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    points= db.Column(db.Integer, nullable=False)
    household= db.Column(db.Integer,db.ForeignKey('household.id'), nullable=False)

    chores= db.relationship("AvailableChore", backref='account', lazy='dynamic')
    def __init__(self, name, username, password, household):
        self.name = name
        self.username = username
        self.password = password
        self.points=0
        self.household= household
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class Household(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(144), nullable=False)
    def __init__(self, name):
        self.name=name
