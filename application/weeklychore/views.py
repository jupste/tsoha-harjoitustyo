from application import app, db
from sqlalchemy import func
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.weeklychore.forms import WeeklyForm
from application.weeklychore.models import WeeklyChore
from application.households.models import Household

@app.route("/weeklychores/", methods=["GET"])
@login_required
def weekly_index():
    h = Household.query.get(current_user.household)
    return render_template("/weeklychores/list.html", weeklychores = h.weekly_chores)

@app.route("/weeklychores/new/")
@login_required
def weekly_form():
    return render_template("/weeklychores/new.html", form=WeeklyForm())

@app.route("/weeklychores/show/<weekly_id>", methods=["GET"])
@login_required
def show_weekly(weekly_id):
    return render_template("weeklychores/show.html", weekly=WeeklyChore.query.get(weekly_id), form=WeeklyForm())

@app.route("/weeklychores/deletion/<weekly_id>" , methods=["POST"])
@login_required
def delete_weekly(weekly_id):
    weekly=WeeklyChore.query.get(weekly_id)
    db.session().delete(weekly)
    db.session().commit()
    return redirect(url_for("weekly_index"))

@app.route("/weeklychores/new/", methods=["POST"])
@login_required
def weekly_create():
    form = WeeklyForm(request.form)
    if not form.validate():
        return render_template("weeklychores/new.html", form = form)
    weekly = WeeklyChore(form.choretype.data, current_user.household, form.interval.data, form.points.data)
    db.session.add(weekly)
    db.session().commit()
    return redirect(url_for("weekly_index"))

@app.route("/weeklychores/edit/<weekly_id>", methods=["POST"])
@login_required
def edit_weekly(weekly_id):
    form = WeeklyForm(request.form)
    weekly= WeeklyChore.query.get(weekly_id)
    weekly.interval=form.interval.data
    weekly.points=form.points.data
    db.session().commit()
    return redirect(url_for("weekly_index"))