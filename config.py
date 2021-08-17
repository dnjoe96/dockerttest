# the essense of creating a configuration setting app seperately
# from the other files or the file that was used to create application
# is for the purpose of simplicity. and best practice.


# so we import os
import os


basedir = os.path.abspath(os.path.dirname(__file__))

# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql://user1:Praise@1234@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # to disable the feature of flasSQAlcheny that signals apllication each time a change is made



class Development_config(Config):

    DEBUG = True
    SQLALCHEMY_ECHO = True

class Production_config(Config):

    DEBUG = False