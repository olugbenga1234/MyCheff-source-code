from flask import Blueprint, render_template, request, redirect, url_for, Flask, flash, Markup
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from src.extensions import db
from src.models import User, Cheffservice
# from flask_wtf.file import FileField, FileAllowed


SECRET_KEY = '1234567890'
auth = Blueprint('auth', __name__)

# function for register


@auth.route('/register', methods=['GET', 'POST'])
@auth.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        unhashed_password = request.form.get('password')
        city = request.form.get('city')
        location = request.form.get('location')
        usertype = request.form.get('usertype')

# check if username exists
        checkusername = User.query.filter_by(username=username).first()

        if checkusername:
            flash(Markup(' Username already exists. Already have an account?<a href="login.html" style="color: yellow; font-weight: 900;"> Login In</a>'), 'error')
            return redirect(url_for('auth.register'))

        new_user = User(lastname=lastname,
                        firstname=firstname,
                        username=username,
                        unhashed_password=unhashed_password,
                        city=city,
                        location=location,
                        usertype=usertype
                        )

        db.session.add(new_user)
        db.session.commit()

        flash(' Registered successfully', 'success')

        return redirect(url_for('auth.login'))

    return render_template('register.html')


# function for login
@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(Markup(' Already Logged In, click<a href="logout.html" style="color: yellow; font-weight: 900;"> HERE </a> to Logout.'), 'error')

        return redirect(url_for('auth.logout'))

    elif request.method == 'POST':
        username = request.form.get("username", False)
        password = request.form['password']
        remember = True if request.form.get('remember') else False

# validate details
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash(Markup(' Could not Login, Please check your login details and try again! Or click <a href="register.html" style="color: yellow; font-weight: 900;"> HERE </a> to register.'), 'error')
            return redirect(url_for('auth.login'))
        else:
            login_user(user, remember=remember)
            return redirect(url_for('main.index'))

    return render_template('login.html')


# logout user
@auth.route('/logout')
@auth.route('/logout.html')
def logout():
    logout_user()
    flash('Logged Out successfully', 'success')
    return redirect(url_for('auth.login'))
