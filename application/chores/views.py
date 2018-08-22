from application import app, db, login_required
from sqlalchemy import func
from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application.chores.models import AvailableChore
from application.donechores.models import DoneChore
from application.chores.forms import ChoreForm
from application.households.models import Household

@app.route("/chores/", methods=["GET"])
@login_required(role="ANY")
def chore_index():
    h = Household.query.get(current_user.household)
    return render_template("/chores/list.html", avchores = h.chores.filter(AvailableChore.points>0))

@app.route("/chores/new/")
@login_required(role="ANY")
def chore_form():
    return render_template("/chores/new.html", form=ChoreForm())

@app.route("/chores/show/edit/<chore_id>", methods=["POST"])
@login_required(role="ANY")
def edit_message(chore_id):
    form = ChoreForm(request.form)
    chore= AvailableChore.query.get(chore_id)
    chore.message=form.message.data
    db.session().commit()
    return render_template("chores/show.html", chore=AvailableChore.query.get(chore_id), form=ChoreForm())

@app.route("/chores/show/<chore_id>/" , methods=["GET"])
@login_required(role="ANY")
def show_chore(chore_id):
    return render_template("chores/show.html", chore=AvailableChore.query.get(chore_id), form=ChoreForm())

@app.route("/chores/secret/",  methods=["GET"])
@login_required(role="Boss")
def secret_backdoor():
    h=Household.query.filter(AvailableChore.points>0).all()
    return render_template("/chores/list.html", avchores=h)

@app.route("/chores/deletion/<chore_id>/" , methods=["POST"])
@login_required(role="ANY")
def delete_chore(chore_id):
    chore=AvailableChore.query.get(chore_id)
    if(chore.points==chore.maxpoints):
        db.session().delete(chore)
        db.session().commit()
    return redirect(url_for("chore_index"))

@app.route("/chores/", methods=["POST"])
@login_required(role="ANY")
def chore_create_custom():
    form = ChoreForm(request.form)
    if not form.validate():
        return render_template("chores/new.html", form = form)
    chore = AvailableChore(current_user.household, form.points.data, form.choretype.data)
    chore.message=form.message.data
    db.session.add(chore)
    db.session().commit()
    return redirect(url_for("chore_index"))