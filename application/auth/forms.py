#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

households= [(1,'TestiTalo')]

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana", [validators.Length(min=5, message= "Liian lyhyt salasana")])
    household = SelectField("Kotitalous", choices=households)
    class Meta:
        csrf = False