from app.api.resources.resources import PasswordFactory
from dotenv import dotenv_values
from flask_restful import Api
from app.logger import Logger
from flask_cors import CORS
from flask import Flask
import os

# create flask app instance
app = Flask(__name__)

# setup logger in the beginning to catch errors
logger = Logger(name="applogger").get_logger()

# makes sure cross origin headers are added
CORS(app)

# initiate instance of flask-restful
# add the only resource to generate password
# link with flask through api.init_app
api = Api()
api.add_resource(PasswordFactory, "/generate")
api.init_app(app)

logger.info("Application is initialised successfully")
try:
    # environment varibales overrides .env file
    config = {
        **dotenv_values(".env"),
        **os.environ,
    }

    # get the env varibales and pass it to app config
    app.config.from_prefixed_env(prefix="PASSWORD")
    logger.info("Added environment varibales to the app")
except Exception as e:
    logger.info("Error occurred while parsing env varibales.")
    app.logger.exception(e)


@app.after_request
def add_security_headers(response):
    """
    Make sure to add security headers to each API response

    """
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response
