from flask_login import UserMixin, login_required, login_manager
from werkzeug.security import generate_password_hash
from .extensions import db, app
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import date, datetime
# import json

# User Account Model


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    password = db.Column(db.String(200))
    username = db.Column(db.String(100), unique=True)
    location = db.Column(db.Text)
    city = db.Column(db.String(80))
    usertype = db.Column(db.String)

    cheffservice = db.relationship(
        'Cheffservice',
        backref='cheffservice', 
        uselist=False,
        lazy=True)

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(
            unhashed_password, method='sha256')

    def __repr__(self):
        return '<User %r>' % self.username


# cheff service database
class Cheffservice(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)
    # cheff price
    cheff_price = db.Column(db.Integer)
    # cheff service description
    cheff_description = db.Column(db.String(900))
    # posted by id
    posted_by_id = db.Column(
        db.Integer, db.ForeignKey('user.id'))
    # date created
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    # cheff city
    city = db.Column(db.String(300))

    # image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    # image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    # image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')
    # image_4 = db.Column(db.String(150), nullable=False, default='image.jpg')
