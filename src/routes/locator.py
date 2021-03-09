#from geopy.geocoders import Nominatim
from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for, Markup
#from geopy.distance import geodesic, great_circle
#from geopy import distance
from src.models import User
from src.extensions import db


app = Flask(__name__)

app = Flask(__name__)

main = Blueprint('main', __name__)

locator = Blueprint('locator', __name__)


# distance
#@locator.route('/locatorr/<str:city>')
@locator.route('/locatorr.html', methods=['GET', 'POST'])
def distance(city):
    if request.method == 'POST':
        ucity = request.form.get('city')
        page = request.args.get('page', 1, type=int)
        products = User.query.filter(
            User.city == ucity).paginate(page=page, per_page=4)
        get_cat = User.query.filter_by(city=ucity).first_or_404()
        get_cat_prod = User.query.filter_by(
            city=get_city).paginate(page=page, per_page=4)

        # get locations from database
        checklocation = User.query.filter(User.city == city).all()

        for cheff_location in checklocation:
            print(cheff_location.username)

        # print(checklocation)

        return redirect(url_for('main.new'))

    return render_template('locator.html', get_cat_prod=get_cat_prod, categories=categories, get_cat=get_cat, products=products
                           )
# distance
# @locator.route('/locator')
# @locator.route('/locator.html', methods=['GET', 'POST'])
# def distance():
    # if request.method == 'POST':
    #uLat = request.form.get('uLat')
    #uLon = request.form.get('uLon')

    # uLat = "39.38383"
    # uLon = "-9.3733"

    # # get locations from database
    # cheffs = User.query.filter(User.coordinates).all()

    # for cheff_coord in cheffs:
    #     print(cheff_coord.coordinates)

    #     cCoord = cheff_coord.coordinates
    #     #cCoord = "51.45685,-0.01126"
    #     uCoord = "89.38383,-9.3733"

    # print(great_circle(cCoord, uCoord).miles)

    # return redirect(url_for('main.new'))

    # return render_template('locator.html')
