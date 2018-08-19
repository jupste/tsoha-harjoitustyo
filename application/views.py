from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lazy")
def lazy_users():
    return render_template("lazy.html", lazy= User.find_lazy_users())
