import os


class Config(object):
    Secret_KEY = os.environ.get("SECRET_KEY" or 'a-string-you-will-never-guess')
