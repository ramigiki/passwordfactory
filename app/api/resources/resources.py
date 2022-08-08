from flask_restful import Resource
from app.api.schema import PasswordReqSchema
from marshmallow.exceptions import ValidationError
from app.api.utilities import generate_password
from flask import request, Response
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
        """
        request_schema = PasswordReqSchema()
        args = request.args.to_dict()
        try:
            data = request_schema.load(args)
            password = generate_password(**data)
            response = {"password": password}
            return Response(
                json.dumps(response), status=200, mimetype="application/json"
            )
        except ValidationError as err:
            return Response(json.dumps(err.messages), status=400)
