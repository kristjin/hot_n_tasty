import os

# Flask-Script Manager class for adding command line arguments easily
from flask.ext.script import Manager

from getpass import getpass
from werkzeug.security import generate_password_hash

# Created in __init__.py; the Flask application at large
from tasty import app

from tasty.models import Flavor, User
from tasty.database import session


manager = Manager(app)

@manager.command
def adduser():
    name = raw_input("Name: ")
    email = raw_input("Email: ")
    if session.query(User).filter_by(email=email).first():
        print("user with that email address already exists")
        return
    admin = ""
    while not (admin == "y" or admin == "n"):
        admin = raw_input("Admin? (y or n)")
    if admin == "y":
        admin = True
    elif admin == "n":
        admin = False
    password = ""
    password_2 = ""
    while not (password and password_2) or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(name=name, email=email,
                password=generate_password_hash(password),
                admin=admin
                )
    session.add(user)
    session.commit()


@manager.command
def seed():
    flavors = ['eggs', 'bacon', 'bananas', 'chocolate', 'macadamia nuts', 'rum']
    for name in flavors:
        f = Flavor(name=name)
        session.add(f)
        session.commit()


@manager.command
def run():
    # Attempt to retrieve port # from environment
    # - Many hosts will use this to identify proper port -
    # If not available, default to 8080
    port = int(os.environ.get('PORT', 8080))
    # Run the app on the dev server, listening on assigned port
    app.run(host='0.0.0.0', port=port)

# This is what runs if the script is run from the command line
# In it, we call the manager instance created above
# This is better than creating our own argparse
if __name__ == "__main__":
    manager.run()
