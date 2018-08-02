from application import app, db
from sqlalchemy import func
from flask import render_template, request, url_for, redirect
from application.available_chores.models import AvailableChore
from application.available_chores.models import User
from application.available_chores.models import DoneChore
user=1

@app.route("/available_chores", methods=["GET"])
def tasks_index():
   if(db.session.query(User).count()==0):
       u=User("TestiSeppo")
       db.session.add(u)
       db.session.commit()
   return render_template("/available_chores/list.html", avchores = AvailableChore.query.filter(AvailableChore.points>0))

@app.route("/available_chores/new/")
def tasks_form():
    return render_template("/available_chores/new.html")

@app.route("/available_chores/<chore_id>/", methods=["POST"])
def chore_do_partially(chore_id):
    chore = AvailableChore.query.get(chore_id)
    if(chore.points>0):
        chore.points = chore.points-1
        d= DoneChore(1, chore.id, 1)
        db.session.add(d)
        db.session.commit()        
    db.session().commit()
    return redirect(url_for("tasks_index"))

@app.route("/available_chores/<chore_id>/", methods=["POST"])
def chore_do_fully(chore_id):
    t = AvailableChore.query.get(chore_id)
    user = User.query.filter(User.id==1)
    t.points = 0
    db.session().commit()
    return redirect(url_for("tasks_index"))

@app.route("/available_chores/", methods=["POST"])
def tasks_create():
    chore=AvailableChore(1)
    db.session.add(chore)
    db.session().commit()
    return redirect(url_for("tasks_index"))
