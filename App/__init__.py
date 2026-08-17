from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
migrate = Migrate()
swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda model: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "rute",
            "description": "rute identifier",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
            }
        }
    }
swagger = Swagger(config=swagger_config, template=swagger_template)

