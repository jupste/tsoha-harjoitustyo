from flask import render_template
from application import app
from application.auth.models import User
from application.weeklychore.views import add_weekly_chores
from application.choretype.views import initialize_choretypes

@app.route("/")
def index():
    add_weekly_chores()
    initialize_choretypes()
    return render_template("index.html")

@app.route("/lazy")
def lazy_users():
    return render_template("lazy.html", lazy= User.find_lazy_users())
