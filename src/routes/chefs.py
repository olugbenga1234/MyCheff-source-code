from flask import Blueprint, render_template, request, redirect, url_for, Flask, flash, Markup, session, current_app, make_response
from src.extensions import db
from flask_login import login_user, logout_user, current_user, login_required
from src.models import User, Cheffservice
import os

SECRET_KEY = '1234567890'
chefs = Blueprint('chefs', __name__)


# display chefs based on city
@chefs.route('/city/<city>', methods=['GET', 'POST'])
def get_city(city):
    ucity = city
    # return city
    page = request.args.get('page', 1, type=int)
    cheffservice = Cheffservice.query.filter_by(
        city=city).paginate(page=page, per_page=3)

    return render_template('chef.html', cheffservice=cheffservice)


# display all chefs
@chefs.route('/chefs', methods=['GET', 'POST'])
@chefs.route('/chefs.html', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        ucity = request.form.get('city')
        return redirect(url_for('chefs.get_city', city=ucity))

    page = request.args.get('page', 1, type=int)

    cheffservice = Cheffservice.query.filter(
        Cheffservice.city != 'null').paginate(page=page, per_page=3)

    return render_template('chef.html', cheffservice=cheffservice)


# cheffservice details
@chefs.route('/service/<int:id>')
def single_page(id):
    cheffservice = Cheffservice.query.get_or_404(id)
    #cheff = User.query.all()

    return render_template('single_page.html', cheffservice=cheffservice)


# Add service
@chefs.route('/addservice', methods=['GET', 'POST'])
@chefs.route('/addservice.html', methods=['GET', 'POST'])
@login_required
def addservice():

    if request.method == 'POST':
        cheff_price = request.form.get('price')
        city = request.form.get('city')
        cheff_description = request.form.get('description')

        addserv = Cheffservice(
            posted_by_id=current_user.id,
            cheff_price=cheff_price,
            cheff_description=cheff_description,
            city=city
            # image_1=image_1,
            # image_2=image_2,
            # image_3=image_3,
            # image_4=image_4

        )

        db.session.add(addserv)
        db.session.commit()

        flash(f'The product {current_user.username} has been added', 'success')

        return redirect(url_for('chefs.services'))

    return render_template('new.html')
