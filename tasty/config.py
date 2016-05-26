import ConfigParser

cfg = ConfigParser.RawConfigParser()
cfg.read('./tasty/tasty.cfg')

class DevelopmentConfig(object):
    # Tell SQLAlchemy where to find the database
    SQLALCHEMY_DATABASE_URI = cfg.get("postgreSQL","DATABASE_URI")
    # Tell Flask whether to use Debug mode for tracking down errors
    DEBUG = cfg.getboolean("flask", "DEBUG")
    # Provide a secret key for tasty (used by? eh?)
    SECRET_KEY = cfg.get("tasty","TASTY_SECRET_KEY")


class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = cfg.get("testing", "SQLALCHEMY_DATABASE_URI")
    DEBUG = cfg.getboolean("testing", "DEBUG")
    SECRET_KEY = cfg.get("testing", "TASTY_SECRET_KEY")
