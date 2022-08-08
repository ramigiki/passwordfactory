from marshmallow import Schema, fields, validate, pre_load
from marshmallow.exceptions import ValidationError
from flask import current_app


class PasswordReqSchema(Schema):
    """
    Marshmallow schema for password api call

    Args:
        Schema (Schema): Inherits base schema class

    Raises:
        ValidationError: If the api args donot conform

    """

    length = fields.Integer(validate=validate.Range(min=5, max=200))
    generic_validator = validate.OneOf(choices=[0, 1])

    numbers = fields.Integer(validate=generic_validator)
    symbols = fields.Integer(validate=generic_validator)
    lowercase = fields.Integer(validate=generic_validator)
    uppercase = fields.Integer(validate=generic_validator)

    @property
    def fields_dict(self):
        """
        Convert schema fields to dictionary

        """
        return self._declared_fields

    @pre_load
    def populate_from_env(self, data, **kwargs):
        """
        Get the default args from the server incase missing in request

        Args:
            data (dict): request data
            fill the missing configs in request from the env variables

        Returns:
            data (dict): returns complete data
        """

        if "symbols" not in data:
            data["symbols"] = current_app.config["SPECIAL_SYMBOLS"]
        if "lowercase" not in data:
            data["lowercase"] = current_app.config["LOWER_CASE"]
        if "uppercase" not in data:
            data["uppercase"] = current_app.config["UPPER_CASE"]
        if "length" not in data:
            data["length"] = current_app.config["LENGTH"]
        if "numbers" not in data:
            data["numbers"] = current_app.config["NUMBERS"]
        return data

    @pre_load
    def validate_features(self, data, **kwargs):
        """
        Makes sure that atleat one feature is enabled

        Args:
            data (dict): request params

        Raises:
            ValidationError: if all the features are disabled

        Returns:
            data (dict): returns data dict
        """
        low = "lowercase" in data and int(data["lowercase"]) == 0
        upp = "uppercase" in data and int(data["uppercase"]) == 0
        sym = "symbols" in data and int(data["symbols"]) == 0
        num = "numbers" in data and int(data["numbers"]) == 0
        if num and sym and low and upp:
            message = "Atleast one feature should be active"
            raise ValidationError(message=message, field_name="all")
        return data
