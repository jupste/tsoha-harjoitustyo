#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.auth.models import User
from application.households.forms import HouseholdForm
from application.households.models import Household
from application.auth.views import register_form

@app.route("/auth/household")
def household_form():
    return render_template("/households/household.html", form=HouseholdForm())


@app.route("/auth/household", methods=["POST"])
def add_household():
    form = HouseholdForm()
    household = Household(form.name.data)
    db.session.add(household)
    db.session().commit()
    return redirect(url_for("register_form"))
