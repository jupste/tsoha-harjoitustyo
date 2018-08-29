#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_login import login_user, logout_user
from application import app, db, login_required
from application.choretype.models import Choretype

@app.route("/choretypes/init", methods=["POST"])
@login_required(role="Boss")
def initialize_choretypes():
    choretypes=["Imurointi" , "Tiskaus", "Pyykkien peseminen", "Lemmikkien ulkoiluttaminen", "Mattojen tamppaus", "Pölyjen pyyhkiminen"]
    for type in choretypes:
        t= Choretype(type)
        db.session().add(t)
        db.session().commit()
