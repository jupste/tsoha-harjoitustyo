from flask import render_template
from application import app
from application.auth.models import User
from application.weeklychore.views import add_weekly_chores
from application.choretype.views import initialize_choretypes

@app.route("/")
def index():
    add_weekly_chores()
    return render_template("index.html")

