from flask import Flask, request, make_response, abort, \
                render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from forms import NameForm
from flask_sqlalchemy import SQLAlchemy
# from models import User, Role


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config["SECRET_KEY"] = "hard to guess"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:passme@localhost/flasky"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role %r>" % self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/")
def index():
    return render_template('index.html', data=[1,2,3], current_time=datetime.utcnow())

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name='leninlal')

@app.route("/test/form",methods=["GET","POST"])
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
        return redirect(url_for('render_test_form'))
    return render_template('test_form.html', form=form, name=session.get('name'), known=session.get('known',False))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    manager.run()