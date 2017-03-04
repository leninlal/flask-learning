from . import mail
from flask import render_template, current_app


def send_email(to_email,subject,template,**kwargs):
    print render_template(template+'.html',**kwargs)
    mail.send_email(
    	from_email = current_app.config['SENDGRID_DEFAULT_FROM'],
    	to_email = to_email,
    	subject = subject,
    	text = render_template(template+'.html',**kwargs)
    	)
