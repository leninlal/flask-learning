from flask import request, make_response, abort, \
                render_template, session, redirect, url_for, flash
from datetime import datetime
from .forms import NameForm
from .. import db
from ..models import User
from . import main

@main.route("/")
def index():
    return render_template('index.html', data=[1,2,3], current_time=datetime.utcnow())

@main.route("/user/<name>")
def user(name):
    return render_template('user.html', name='leninlal')

@main.route("/test/form",methods=["GET","POST"])
def render_test_form():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.render_test_form'))
    return render_template('test_form.html', form=form, name=session.get('name'), known=session.get('known',False))
