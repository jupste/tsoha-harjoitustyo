#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

households= [(1,'TestiTalo'),(2, 'Hullujen huone')]

class UserForm(FlaskForm):
    name= StringField("Nimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana", [validators.Length(min=4, message= "Liian lyhyt salasana")])
    household = SelectField("Kotitalous", choices=households)
    class Meta:
        csrf = False