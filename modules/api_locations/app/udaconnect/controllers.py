from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from app.udaconnect.services import LocationService
from flask import abort
from flask_accepts import responds
from flask_restx import Namespace, Resource
import logging

api = Namespace("UdaConnect", description="Connections via geolocation - Locations API.")
location_fields = Location.get_location_fields(api)
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-locations-api")

@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    """ Location Data Resource

    Args:
        Resource (Resource): flask_restx Resource class

    """
    @responds(schema=LocationSchema)
    @api.doc(description = "Return a location object based on the given location id", responses={200: 'Returns a location object', 404: 'Location object not found'})
    @api.marshal_with(location_fields)
    def get(self, location_id) -> Location:
        """ Get the related location object from the DB based on the given location id

        Args:
            location_id (int): The Location entry id

        Returns:
            Location: The found location object
        """
        location: Location = LocationService.retrieve(location_id)
        if location is None:
            logger.error('There is not location entry in the DB with the given location id.')
            abort(404, "Location not found")
        return location