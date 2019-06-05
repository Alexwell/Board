# -*- coding: utf-8 -*-

from wtforms_alchemy import ModelForm

from app.models import Book, Comments


class BookForm(ModelForm):
    class Meta:
        model = Book


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        include = [
            'first_id'
        ]
