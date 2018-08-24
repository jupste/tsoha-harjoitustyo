from flask import render_template
from application import app
from application.auth.models import User
from application.weeklychore.views import add_weekly_chores

@app.route("/")
def index():
    add_weekly_chores()
    return render_template("index.html")

@app.route("/lazy")
def lazy_users():
    return render_template("lazy.html", lazy= User.find_lazy_users())
