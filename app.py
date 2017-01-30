from flask import Flask, request, make_response, abort, \
                render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from forms import NameForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config["SECRET_KEY"] = "hard to guess"
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
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash("looks like u have changed your name")
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('render_test_form'))
    return render_template('test_form.html', form=form, name=session.get('name'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    manager.run()