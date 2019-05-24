# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


if __name__ == '__main__':
    from models import *
    db.create_all()

    # if User.query.count() == 0:
    # 	populate_db()

    users = User.query.all()
    print(list(map(str, users)))

    app.run()
