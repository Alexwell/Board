# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        from models import Book
        posts = Book.query.all()

        for post in posts:
            user_id = post.id
            user_name = post.author
            user_text = post.text
            user_date = post.date_created
            print(post.id, post.author, post.text, post.date_created)

        return render_template('home.html', posts=posts), 200

    else:
        return "Wrong input", 404


@app.route('/create', methods=['GET', 'POST'])
def create():
    from models import Book
    from forms import BookForm

    if request.method == 'POST':
        form = BookForm(request.form)

        if form.validate():
            post = Book(**form.data)
            db.session.add(post)
            db.session.commit()

            return ('Post created'), 200
        else:
            return ('Not valid'), 200
    else:
        return 'Wrong response', 404


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    from models import Comments
    from forms import CommentForm

    if request.method == 'POST':
        form_comment = CommentForm(request.form)

        if form_comment.validate():
            post_comment = Comments(**form_comment.data)
            db.session.add(post_comment)
            db.session.commit()

            return ('Comment created'), 200
        else:
            return ('Not valid comment'), 200
    else:
        return 'Wrong comment response', 404


if __name__ == '__main__':
    from models import *
    db.create_all()
    app.run()
