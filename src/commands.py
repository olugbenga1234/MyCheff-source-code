import click
from flask.cli import with_appcontext

from .extensions import db
from .models import User, Cheffservice


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

    new_user = User(lastname="Adriano",
                    firstname="Mike",
                    username="mike",
                    unhashed_password="user1",
                    city="London",
                    location="location",
                    usertype="chef"
                    )
    db.session.add(new_user)
    db.session.commit()

    new_user1 = User(lastname="Susan",
                     firstname="Joe",
                     username="susan",
                     unhashed_password="user1",
                     city="Paris",
                     location="location",
                     usertype="chef"
                     )
    db.session.add(new_user1)
    db.session.commit()

    new_user2 = User(lastname="Joe",
                     firstname="John",
                     username="joe",
                     unhashed_password="user2",
                     city="London",
                     location="location",
                     usertype="chef"
                     )
    db.session.add(new_user2)
    db.session.commit()

    new_user2 = User(lastname="Danokun",
                     firstname="Fester",
                     username="fester",
                     unhashed_password="user3",
                     city="Newyork",
                     location="location",
                     usertype="chef"
                     )
    db.session.add(new_user3)
    db.session.commit()


# @click.command(name='users')
# @with_appcontext
# def users():
#     new_user = User(lastname="Adriano",
#                     firstname="Mike",
#                     username="mike",
#                     unhashed_password="user1",
#                     city="London",
#                     location="location",
#                     usertype="chef"
#                     )

#     new_user = User(lastname="Adriano",
#                     firstname="Mike",
#                     username="mike1",
#                     unhashed_password="user1",
#                     city="London",
#                     location="location",
#                     usertype="chef"
#                     )
#     db.session.add(new_user)
#     db.session.commit()
