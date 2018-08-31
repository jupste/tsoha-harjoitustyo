#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, validators, IntegerField
from application.choretype.models import Choretype

class ChoreForm(FlaskForm):
    choretypes=[]
    choretype = SelectField(label="Kotityö", validators=[validators.DataRequired(message="Pääkäyttäjän pitää käydä alustamassa kotityötyyppien lista")], choices=choretypes)
    points = IntegerField(label="Pisteet", validators=[validators.NumberRange(message="Pisteet väliltä 1-10", min=1, max=10)])
    message = StringField(label="Viesti")
    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super(ChoreForm, self).__init__(*args, **kwargs)
        self.choretype.choices = [(str(c.id), c.name) for c in Choretype.query.all()]
