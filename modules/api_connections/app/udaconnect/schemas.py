from app.udaconnect.models import Location, Person
from marshmallow import Schema, fields

class LocationSchema(Schema):
    """ Location schema

    Args:
        Schema (Schema): Marshmallow schema class
    """
    id = fields.Integer()
    person_id = fields.Integer()
    longitude = fields.String(attribute="longitude")
    latitude = fields.String(attribute="latitude")
    creation_time = fields.DateTime()

    class Meta:
        model = Location


class PersonSchema(Schema):
    """ Person schema

    Args:
        Schema (Schema): Marshmallow schema class
    """
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()

    class Meta:
        model = Person

class ConnectionSchema(Schema):
    """ Connection schema

    Args:
        Schema (Connection): Marshmallow schema class
    """
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
