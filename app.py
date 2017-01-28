from flask import Flask, request, make_response, abort, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
@app.route("/")
def index():
	return render_template('index.html', data=[1,2,3])

@app.route("/user/<name>")
def user(name):
	return render_template('user.html', name='leninlal')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	manager.run()