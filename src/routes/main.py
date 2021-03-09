from flask import Blueprint, render_template, request, jsonify, json, redirect, flash, url_for, Markup
from flask_login import login_required, current_user
from flask import Flask

# from opencage.geocoder import OpenCageGeocode
# from pprint import pprint
# from src.routes.auth import UpdateAccountForm
from src.extensions import db
# from src.models import Donated, User
from src.models import User
# import secrets
# import smtplib
# import os

# from PIL import Image
# from flask_mail import Mail
# from email.message import EmailMessage

app = Flask(__name__)

main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)


# home
@main.route('/')
@main.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        location = request.form.get('location')
        city = request.form.get('city')
        #coordinates = request.form.get('cheff_coord')

        new = User(username=username,
                   location=location,
                   city=city,
                   # coordinates=coordinates
                   )

        db.session.add(new)
        db.session.commit()

        return redirect(url_for('main.new'))
    return render_template('index.html')
