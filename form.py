# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField


class requstform(FlaskForm):
    ticker = StringField('Ticker Symbol:')
    cp_Flag = BooleanField('Closing price')
    acp_Flag = BooleanField('Adjusted closing price')
    op_Flag = BooleanField('Open price')
    aop_Flag = BooleanField('Adjusted open price')
    submit = SubmitField('Submit')