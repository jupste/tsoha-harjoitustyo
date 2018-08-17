#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.auth.models import User
from application.auth.models import Household
from application.auth.forms import UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = UserForm())

    form = UserForm(request.form)
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/household")
def household_form():
    return render_template("/auth/household.html", form=UserForm())

@app.route("/auth/household", methods=["POST"])
def add_household():
    form = UserForm()
    household = Household(form.name.data)
    db.session.add(household)
    db.session().commit()
    return redirect(url_for("register_form"))

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
#    if not form.validate():
#        return render_template("auth/register.html", form = form)
    user = User(form.name.data, form.username.data, form.password.data, form.household.data)
    db.session.add(user)
    db.session().commit()
    return render_template("auth/loginform.html", form=UserForm())
