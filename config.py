import os


class Config(object):

    """main config obj for app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'M7cwkj?2019'
