from application import app, db
from flask import render_template, request, url_for, redirect
from application.available_chores.models import Avchore

@app.route("/available_chores", methods=["GET"])
def tasks_index():
    return render_template("/available_chores/list.html", avchores = Avchore.query.filter(Avchore.points>0))

@app.route("/available_chores/new/")
def tasks_form():
    return render_template("/available_chores/new.html")

@app.route("/available_chores/<avchore_id>/", methods=["POST"])
def chore_do_partially(avchore_id):

    t = Avchore.query.get(avchore_id)
    if(t.points>0):
        t.points = t.points-1
    db.session().commit()
    return redirect(url_for("tasks_index"))

@app.route("/available_chores/", methods=["POST"])
def tasks_create():
    t=Avchore(request.form.get("name"))
    db.session.add(t)
    db.session().commit()
    return redirect(url_for("tasks_index"))
