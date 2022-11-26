from datetime import datetime
from app.udaconnect.models import Connection
from app.udaconnect.schemas import ConnectionSchema
from app.udaconnect.services import ConnectionService
from flask import request, abort
from flask_accepts import responds
from flask_restx import Namespace, Resource
from typing import Optional
import logging

'''
    Contains all the routes of the udaconnect connections api.
'''

DATE_FORMAT = "%Y-%m-%d"
api = Namespace("UdaConnect", description="Connections via geolocation - Connections API.")
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-connections-api")

connection_fields = Connection.get_connection_fields(api)

@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    """ Connection Data Resource

    Args:
        Resource (Resource): flask_restx Resource class

    """
    @responds(schema=ConnectionSchema, many=True)
    @api.doc(description="Returns all the persons who have been within a given distance of a given Person within a date range pluse the related locations.", responses={ 200: 'Return all the related persons and locations', 400: 'Failed to retrieve related connections.' })
    @api.marshal_with(connection_fields, as_list=True)
    def get(self, person_id) -> ConnectionSchema:
        """ Get person connections based on the given person id

        Args:
            person_id (int): The person id

        Returns:
            List[Connection]: A list of the related connections_
        """
        try:
            start_date: datetime = datetime.strptime(
                request.args["start_date"], DATE_FORMAT
            )
            end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
            distance: Optional[int] = request.args.get("distance", 5)

            results = ConnectionService.find_contacts(
                person_id=person_id,
                start_date=start_date,
                end_date=end_date,
                meters=distance,
            )
            
            return results
        except Exception as e:
            logger.error("Failed to retrieve related connections. Details: " + str(e))
            abort(400, "Failed to retrieve related connections.")