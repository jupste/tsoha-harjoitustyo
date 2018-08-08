from application import app, db
from sqlalchemy import func
from flask import render_template, request, url_for, redirect
from flask_login import login_required
from application.available_chores.models import AvailableChore, DoneChore
from application.available_chores.forms import ChoreForm

@app.route("/available_chores/", methods=["GET"])
@login_required
def chore_index():
   return render_template("/available_chores/list.html", avchores = AvailableChore.query.filter(AvailableChore.points>0, AvailableChore.household==1))

@app.route("/available_chores/donechores/", methods=["GET"])
@login_required
def user_index():
    return render_template("/available_chores/userchorelist.html", donechores = DoneChore.query.filter(DoneChore.userid==1))

@app.route("/available_chores/new/")
@login_required
def chore_form():
    return render_template("/available_chores/new.html", form=ChoreForm())

@app.route("/available_chores/<chore_id>/<int:fully>", methods=["POST"])
@login_required
def do_chore(chore_id, fully):
    chore = AvailableChore.query.get(chore_id)
    if(db.session.query(DoneChore.query.filter(DoneChore.id == chore.id).exists()).scalar()):
        donechore=DoneChore.query.get(chore.id)
    else:
        donechore= DoneChore(1, chore.id, 0)
        db.session.add(donechore)
    if(chore.points>0):    
        if(fully):
            score=chore.points
            chore.points = 0            
            donechore.points=donechore.points+score
            db.session.commit()    
        else:
            chore.points=chore.points-1
            donechore.points= donechore.points+1
            db.session.commit()
    return redirect(url_for("chore_index"))

@app.route("/available_chores/", methods=["POST"])
@login_required
def chore_create_custom():
    form = ChoreForm(request.form)
    if not form.validate():
        return render_template("available_chores/new.html", form = form)
    chore = AvailableChore(1, form.points.data, form.choretype.data)
    chore.message=form.message.data
    chore.createdBy=1
    db.session.add(chore)
    db.session().commit()
    return redirect(url_for("chore_index"))