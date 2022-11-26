import logging
from typing import Dict
from app import db
from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from geoalchemy2.functions import ST_Point

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-locations-api")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        """ Load the location object from the database and return based on the given location id.

        Args:
            location_id (int): The id of the location object

        Returns:
            Location: Location object
        """
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location