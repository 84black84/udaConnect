from app.udaconnect.models import Location
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
