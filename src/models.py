# -*- coding: utf-8 -*-

from datetime import date

from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(35))
    text = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Author %r text - %s>' % (self.author, self.text)
