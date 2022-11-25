from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, fields
from typing import List

api = Namespace("UdaConnect", description="Connections via geolocation - Persons API.")
person_fields = api.model('Person', {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'company_name': fields.String
    })

@api.route("/persons", endpoint='persons')
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    @api.doc(responses={201: 'Returns the newly created person object'},  body=person_fields)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person, 201

    @responds(schema=PersonSchema, many=True)
    @api.doc(responses={200: 'Returns a list of all the available person objects'})
    @api.marshal_with(person_fields, as_list=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons

@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
@api.doc("Gets the id of a person as paramter and returns the relater person object")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    @api.doc(responses= { 200: 'Returns a person object based on the given person_id' })
    @api.marshal_with(person_fields)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person
