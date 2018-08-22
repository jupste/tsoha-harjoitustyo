#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

class HouseholdForm(FlaskForm):
    name= StringField("Nimi",[validators.Length(min=2, max=32, message="Nimi pitää olla ainakin 2 ja korkeintaan 32 merkkiä pitkä")])
    
    class Meta:
        csrf = False
