#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db, login_required
from application.auth.models import User
from application.households.forms import HouseholdForm
from application.households.models import Household
from application.auth.forms import UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = UserForm())

    form = UserForm(request.form)
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return render_template("/index.html", topdog=Household.top_dog())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   

@app.route("/auth/register")
def register_form():
    return render_template("/auth/register.html", form=UserForm())

@app.route("/auth/register", methods = ["POST"])
def auth_register():
    form = UserForm()
    if not form.validate_on_submit():
        return render_template("auth/register.html", form = form)
    user = User(form.name.data, form.username.data, form.password.data, int(form.household.data))
    db.session.add(user)
    db.session().commit()
    return render_template("auth/loginform.html", form=UserForm())

@app.route("/auth/lazy")
def lazy_users():
    return render_template("lazy.html", lazy= User.find_lazy_users())

@app.route("/auth/admin")
@login_required(role="Boss")
def admin_view():
    return render_template("auth/admin.html")

