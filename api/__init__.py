from flask import Flask
from flasgger import Swagger
from api.route.auth import auth_api
def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_api)
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Basic Auth & resgitration rest API",
            "description": "API for test dailymotion",
            "contact": {
                "responsibleOrganization": "",
                "responsibleDeveloper": "",
                "email": "haddou.jihad@gmail.com",
                "url": "weberfly-group.com",
            },
            "termsOfService": "weberfly-group.com",
            "version": "1.0"
        },
        "basePath": "/api/v1",  
        "schemes": [
            "http",
            "https"
        ],
    }
    swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/spec"
    }
    Swagger(app=app,config=swagger_config, template=template)
    return app
