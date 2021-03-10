from flask import Flask
from .commands import create_tables
from .extensions import db, login_manager
from .routes.main import main
from .routes.auth import auth
from .routes.chefs import chefs
from .routes.locator import locator
import os
from .models import User, Cheffservice



def create_app(config_file='setting.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Please login to access this page"
    login_manager.login_message_category = "error"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(chefs)

    # admin = Admin(app, name='Admin Dashboard')

    # admin.add_view(ModelView(User, db.session))
    # admin.add_view(ModelView(Donated, db.session))
    # admin.add_view(ModelView(Products, db.session))
    # admin.add_view(ModelView(Category, db.session))
    # admin.add_view(ModelView(CustomerOrder, db.session))

    #migrate = Migrate(app, db)


    app.cli.add_command(create_tables)

    return app
