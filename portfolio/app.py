from flask import Flask

def create_app():
    # Load Flask instance and related setting
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    with app.app_context():
        # Import parts of the application
        from .blueprints.home import home
        from .blueprints.projects import projects
        from .blueprints.blog import blog

        # Register Blueprints
        app.register_blueprint(home.bp)
        app.register_blueprint(projects.bp)
        app.register_blueprint(blog.bp)

        return app