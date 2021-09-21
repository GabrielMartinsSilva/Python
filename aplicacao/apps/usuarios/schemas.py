from marshmallow import Schema, fields, validate, post_load, ValidationError, EXCLUDE
import phonenumbers
from phonenumbers import NumberParseException


class CreateUserSchema(Schema):
    email = fields.Email(required=True)
    nome = fields.Str(required=True, validate=validate.Length(min=1, max=256))
    password = fields.Str(required=True)
    password2 = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    number = fields.Integer(required=False)
    complement = fields.Str(required=False)
    cpf = fields.Str(required=True)

    @post_load
    def validate_password(self, in_data, **kwargs):
        if not in_data["password"] == in_data["password2"]:
            raise ValidationError("Passwords must be equal!", "password_missmatch")
        return in_data
    
    @post_load
    def validate_phone_number(self, in_data, **kwargs):
        if not phonenumbers.is_valid(in_data['phone_number']):
            raise ValidationError("Invalid Phone Number", "phone_number")
        return in_data


    class Meta:
        unknown = EXCLUDE
