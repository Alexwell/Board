# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Book, Comments


class BookForm(ModelForm):
    class Meta:
        model = Book


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        include = [
            'first_id'
        ]
