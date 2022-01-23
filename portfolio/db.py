from flask import current_app

class SimpleDatabase():
    def __init__(self):
        pass

    @classmethod
    def projects(cls):
        return cls()