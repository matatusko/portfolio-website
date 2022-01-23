import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"