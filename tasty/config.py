__author__ = 'kristjin@github'

import ConfigParser

# TODO: This needs to be controlled by moving the file away from the same server somehow.
cfg = ConfigParser.RawConfigParser()
cfg.read('tasty.cfg')


class DevelopmentConfig(object):
    # Tell SQLAlchemy where to find the database
    SQLALCHEMY_DATABASE_URI = cfg.get("postgreSQL","SQLALCHEMY_DATABASE_URI")
    # Tell Flask whether to use Debug mode for tracking down errors
    DEBUG = cfg.getboolean("flask", "DEBUG")
    # Provide a secret key for tasty (used by? eh?)
    SECRET_KEY = cfg.get("tasty","TASTY_SECRET_KEY")
    # Provide an upload folder for tasty (used anywhere at all? I Don't think so.)
    UPLOAD_FOLDER = cfg.get("tasty", "UPLOAD_FOLDER")

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = cfg.get("testing", "SQLALCHEMY_DATABASE_URI")
    DEBUG = cfg.getboolean("testing", "DEBUG")
    SECRET_KEY = cfg.get("testing", "TASTY_SECRET_KEY")
    UPLOAD_FOLDER = cfg.get("testing", "UPLOAD_FOLDER")