from flask_restful import Api
from app.logger import setup_logger
from flask_cors import CORS
from flask import Flask
import sys

# create flask app instance
app = Flask(__name__)
setup_logger()

# makes sure cross origin headers are added
CORS(app)

# initiate instance of flask-restful
# add the only resource to generate password
# link with flask through api.init_app

app.logger.info("Application is initialised, parsing env ...")
try:
    # get the env varibales and pass it to app config
    app.config.from_prefixed_env(prefix="PASSWORD")
    app.logger.info("Added environment varibales to the app")
except Exception as e:
    app.logger.critical("Error occurred while parsing env: {}".format(e))
    sys.exit(1)

# makes sure the circular dependency does not rise
from app.api import PasswordFactory  # noqa E402

api = Api()
api.add_resource(PasswordFactory, "/generate")
api.init_app(app)


@app.after_request
def add_security_headers(response):
    """
    Make sure to add security headers to each API response

    """
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["content-type"] = "application/json"
    return response
