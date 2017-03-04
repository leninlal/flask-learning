from flask import request, make_response, abort, \
                render_template, session, redirect, url_for, flash
from datetime import datetime
from .forms import NameForm
from .. import db
from ..models import User
from . import main

@main.route("/",methods=["GET","POST"])
def index():
    return render_template('index.html')
