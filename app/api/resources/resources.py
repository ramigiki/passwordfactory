from flask_restful import Resource
from app.api.schema import PasswordReqSchema
from marshmallow.exceptions import ValidationError
from app.api.utilities import generate_password
from flask import request, Response
from app import app
import json


class PasswordFactory(Resource):
    """
    Password factory class to server passwords on demand

    """

    def get(self):
        """
        API call to return the generated password

        :param self: Gets default self as the only param
        :returns: Returns password generated
        :generate a formated validation error on incorrect params
        :does not break the application on internal server error
        """
        request_schema = PasswordReqSchema()
        args = request.args.to_dict()
        try:
            data = request_schema.load(args)
            password = generate_password(**data)
            response = {"password": password}
            return Response(json.dumps(response), status=200)
        except ValidationError as verr:
            app.logger.error("Bad request: {}".format(verr.messages))
            error_message = {"error": verr.messages}
            return Response(json.dumps(error_message), status=400)
        except Exception as err:
            app.logger.error(err)
            error_message = {"error": "Internal server error occurred"}
            return Response(json.dumps(error_message), status=500)
