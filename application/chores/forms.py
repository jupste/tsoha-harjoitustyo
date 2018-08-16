#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, validators, IntegerField

choretypes=[("Imurointi","Imurointi") , ("Tiskaus", "Tiskaus"), ("Pyykkien peseminen", "Pyykkien peseminen"), ("Lemmikkien ulkoiluttaminen", "Lemmikkien ulkoiluttaminen"), ("Mattojen tamppaus", "Mattojen tamppaus"), ("Pölyjen pyyhkiminen", "Polyjen pyyhkiminen")]

class ChoreForm(Form):
    choretype = SelectField(label="Kotityö", choices=choretypes)
    points = IntegerField(label="Pisteet", validators=[validators.NumberRange(message="Pisteet valilta 1-10", min=1, max=10)])
    message = StringField(label="Viesti")
    class Meta:
        csrf = False