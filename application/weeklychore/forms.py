#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators, IntegerField
from application.choretype.models import Choretype


class WeeklyForm(FlaskForm):
    choretypes=[]
    choretype= SelectField("Kotityö", validators=[validators.DataRequired(message="Pääkäyttäjän pitää käydä alustamassa kotityötyyppien lista")], choices= choretypes)
    points= IntegerField(label= "Pisteet", validators=[validators.NumberRange(message= "Pisteet pitää olla väliltä 1-5", min=1, max=5)])
    interval= IntegerField(label= "Aikaväli", validators=[validators.NumberRange(message= "Tekoväli pitää olla ainakin 1 päivä ja maksimissaan 30 päivää", min=1, max=30)])
    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super(WeeklyForm, self).__init__(*args, **kwargs)
        self.choretype.choices = [(str(c.id), c.name) for c in Choretype.query.all()]

    