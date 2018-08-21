
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
from application.households.models import Household

class UserForm(FlaskForm):
    households=[]
    h=Household.query.all()
    for house in h:
        households.append((house.id, house.name))
    name= StringField("Nimi",[validators.Length(min=2, max=32, message="Nimi pitää olla ainakin 2 ja korkeintaan 32 merkkiä pitkä")])
    username = StringField("Käyttäjätunnus",[validators.Length(min=2, max=32, message="Käyttäjätunnus pitää olla ainakin 2 ja korkeintaan 32 merkkiä pitkä")])
    password = PasswordField("Salasana", [validators.Length(min=2, max=32, message="Salasanan pitää olla ainakin 2 ja korkeintaan 32 merkkiä pitkä")])
    household = SelectField("Kotitalous", choices=households)
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.household.choices = [(h.id, h.name) for h in Household.query.all()]
    
    class Meta:
        csrf = False
