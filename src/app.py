# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    from models import Book
    # from forms import BookForm
    posts = Book.query.all()

    for post in posts:
        user_id = post.id
        user_name = post.author
        user_text = post.text
        user_date = post.date_created
        print(post.user_id, post.user_name, post.user_text, post.user_date)

    return render_template('home.txt', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create():
    from models import Book
    from forms import BookForm

    if request.method == 'POST':
        form = BookForm(request.form)

        if form.validate():
            post = Book(**fom.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created')
        else:
            flash('Not valid')
            flash(str(form.errors))
    else:
        return 'Page is unavaileble', 404


if __name__ == '__main__':
    from models import *
    db.create_all()

    # if User.query.count() == 0:
    # 	populate_db()

    # users = User.query.all()
    # print(list(map(str, users)))

    app.run()
