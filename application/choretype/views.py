#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_login import login_user, logout_user
from application import app, db
from application.choretype.models import Choretype

def initialize_choretypes():
    choretypes=["Imurointi" , "Tiskaus", "Pyykkien peseminen", "Lemmikkien ulkoiluttaminen", "Mattojen tamppaus", "Pölyjen pyyhkiminen"]
    for type in choretypes:
        t= Choretype(type)
        db.session().add(t)
        db.session().commit()
