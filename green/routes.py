import os 
from flask import render_template, url_for,flash, redirect,abort
from green import app # importing the app from the init.py file (connecting the two)
from green.forms import RegistrationForm, LoginForm
from green.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect (url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=["GET","POST"])
def login():
	# if current_user.is_authenticated:
	# 	return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():		
		if form.email.data == 'email@email.com' and form.password.data == 'password':
			flash(f'Welcome {form.email.data}!')
		# user = User.query.filter_by(email=form.email.data).first()
		# if user and bcrypt.check_password_hash(user.password, form.password.data):
		# 	login_user(user, remember=form.remember.data)
		# 	next_page = request.args.get('next')
		# 	return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html',
							title='Login',
							form=form
							)


