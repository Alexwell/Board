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

        return render_template('home.txt', posts=posts)

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

            return ('Post created')
        else:
            return ('Not valid')
    else:
        return 'Wrong response', 404


if __name__ == '__main__':
    from models import *
    db.create_all()
    app.run()
