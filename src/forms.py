# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
