import os


class Config(object):
    """main config obj for app"""

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'M7cwkj?2019'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CURRENCIES_LIST_URL = 'https://www.banki.ru/products/currency/cb/'
