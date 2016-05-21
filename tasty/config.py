__author__ = 'kristjin@github'

import os


class DevelopmentConfig(object):
    # Tell SQLAlchemy where to find the database
    SQLALCHEMY_DATABASE_URI = "postgresql://kristjin:CatPowers9@localhost:5432/tasty"
    # Tells Flask to use Debug mode for tracking down errors
    DEBUG = True
    # This should go in an external keys file which is part of your .gitignore
    # OR this file should be included and the key can be here
    # But never save a file with your secret keys to git, ever, ever
    SECRET_KEY = os.environ.get("TASTY_SECRET_KEY", "Avwg@Y@25y6u457ijJ7M*jen5$^^P70rk")
    UPLOAD_FOLDER = "uploads"

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://kristjin:CatPowers9@localhost:5432/tasty-test"
    DEBUG = True
    SECRET_KEY = os.environ.get("TASTY_SECRET_KEY", "Not Secret")
    UPLOAD_FOLDER = "test-uploads"