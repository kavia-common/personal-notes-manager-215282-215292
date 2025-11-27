from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from .routes.health import blp as health_blp
from .routes.notes import blp as notes_blp
from .models import db

def create_app():
    """Application factory to create Flask app with configured extensions and routes."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Database configuration: SQLite file under instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # CORS for frontend
    CORS(
        app,
        resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}},
        supports_credentials=False,
    )

    # OpenAPI / Swagger
    app.config["API_TITLE"] = "Notes API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["OPENAPI_REDOC_PATH"] = None

    # Init extensions
    db.init_app(app)

    api = Api(app)
    api.spec.tags = [
        {"name": "Health", "description": "Health check route"},
        {"name": "Notes", "description": "CRUD operations for notes"},
    ]

    # Register blueprints
    api.register_blueprint(health_blp)
    api.register_blueprint(notes_blp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app

# Instantiate the app for WSGI/CLI usage
app = create_app()
api = Api(app)
