from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from app_pkg.routes.home_routes import home_routes
    from app_pkg.routes.rps_routes import rps_routes
    from app_pkg.routes.stocks_routes import stocks_routes

    # Register blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    app.register_blueprint(stocks_routes)

    return app
# this app_pkg/__init__.py file


