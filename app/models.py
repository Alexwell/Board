# -*- coding: utf-8 -*-

from datetime import date

from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(35))
    text = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.Date, default=date.today, nullable=False)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)
    post_comments = db.relationship('Comments', backref='post_comments', lazy='dynamic')

    def __str__(self):
        return '<Author %r text - %s>' % (self.author, self.text)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_comment = db.Column(db.String(35))
    text_comment = db.Column(db.String(300), nullable=False)
    date_created_comment = db.Column(
        db.Date, default=date.today, nullable=False)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)
    first_id = db.Column(
        db.Integer,
        db.ForeignKey('book.id'),
        # nullable=False,
        # index=True,
        # default=1
    )
    # first = db.relationship(Book, foreign_keys=[first_id, ])

    def __str__(self):
        return '<Author %r text - %s>' % (self.author_comment,
                                          self.text_comment)
