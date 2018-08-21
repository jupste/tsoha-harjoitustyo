
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators, IntegerField

choretypes=[("Imurointi","Imurointi") , ("Tiskaus", "Tiskaus"), ("Pyykkien peseminen", "Pyykkien peseminen"), ("Lemmikkien ulkoiluttaminen", "Lemmikkien ulkoiluttaminen"),
 ("Mattojen tamppaus", "Mattojen tamppaus"), ("Pölyjen pyyhkiminen", "Polyjen pyyhkiminen")]
class WeeklyForm(FlaskForm):
    choretype= SelectField(label= "Kotityön tyyppi", choices= choretypes)
    points= IntegerField(label= "Pisteet", validators=[validators.NumberRange(message= "Pisteet pitää olla väliltä 1-5", min=1, max=5)])
    interval= IntegerField(label= "Aikaväli", validators=[validators.NumberRange(message= "Tekoväli pitää olla ainakin 1 päivä ja maksimissaan 30 päivää", min=1, max=30)])
    class Meta:
        csrf = False
