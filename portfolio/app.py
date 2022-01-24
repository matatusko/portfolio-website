import os
from flask import Flask

def create_app():
    # Load Flask instance and related setting
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    # Import parts of the application
    from .home import home
    from .projects import projects
    from .blog import blog

    # Register Blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(blog.bp)

    return app

app = create_app()