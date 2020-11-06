from flask import render_template,flash,request,redirect,url_for,abort
from . import auth
from .forms import Registration,LoginForm
from ..import db,photos
from app.models import Role,Pitch,Review
from flask_login import login_required,current_user,logout_user, login_user
import markdown2
from ..emails import mail_message

#Views
@auth.route('/log-in',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Role.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(Role,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('mai.index'))

        flash('Invalid username or Password')

    title = "Login"
    return render_template('/auth/log-in.html',login_form = login_form,title=title)


@auth.route('/registration',methods = ["GET","POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = Role(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to one minute pitch","email/welcome_user",Role.email,user=user)


        return redirect(url_for('auth.registration'))
    title = "New Account"
    return render_template('./auth/registration.html',registration_form = form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("../templates.index"))