from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	name = StringField('what is ur name', validators=[Required()])
	submit = SubmitField('Submit')