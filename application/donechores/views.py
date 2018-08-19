from application import app, db
from application.chores.models import AvailableChore
from application.donechores.models import DoneChore
from flask import url_for, render_template, redirect
from flask_login import login_required, current_user
from application.chores.views import chore_index

@app.route("/donechores", methods=["GET"])
@login_required
def user_index():
    return render_template("/donechores/userchorelist.html", donechores = DoneChore.user_done_chores())

@app.route("/chores/<chore_id>/<int:fully>" , methods=["POST"])
@login_required
def do_chore(chore_id, fully):
    chore = AvailableChore.query.get(chore_id)
    if not db.session.query(DoneChore.query.filter(DoneChore.id == chore.id).exists()).scalar():
        donechore= DoneChore(current_user.id, chore.id, 0)
        db.session.add(donechore)
    donechore=DoneChore.query.get(chore.id)
    if chore.points>0:    
        if fully:
            score=chore.points
            chore.points = 0            
            donechore.points=donechore.points+score
            db.session.commit()    
        else:
            chore.points=chore.points-1
            donechore.points= donechore.points+1
            db.session.commit()
    return redirect(url_for("chore_index"))