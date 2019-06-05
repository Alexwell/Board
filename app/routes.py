# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.forms import BookForm, CommentForm
from app.models import Book, Comments


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Book.query.all()

        comments = Comments.query.all()

        return render_template('home.html', posts=posts, comments=comments), 200

    else:
        return "Wrong input!!", 404


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = BookForm(request.form)

        if form.validate():
            post = Book(**form.data)
            db.session.add(post)
            db.session.commit()

            return 'Post created', 200
        else:
            return 'Not valid!', 200
    else:
        return 'Wrong response', 404


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':

        form_comment = CommentForm(request.form)

        if form_comment.validate():
            print(form_comment.data)

            post_comment = Comments(**form_comment.data)
            db.session.add(post_comment)
            db.session.commit()
            return f"{form_comment.data['first_id']} Comment created", 200

        else:
            return 'Not valid comment !!', 200

    else:
        return 'Wrong comment response', 404


@app.route('/single_comment/<int:post_id>', methods=['GET', 'POST'])
def single_comment(post_id):
    if request.method == 'GET':
        comments = Comments.query.filter_by(
            first_id=post_id
        )

        return render_template('single_comment.html',
                               post_id=post_id,
                               # posts=posts,
                               comments=comments
                               ), 200
