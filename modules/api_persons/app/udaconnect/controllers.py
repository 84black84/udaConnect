from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService
from flask import request, abort
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

api = Namespace("UdaConnect", description="Connections via geolocation - Persons API.")

person_fields = Person.get_person_fields(api)

@api.route("/persons", endpoint='persons')
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    @api.doc(description="Create a new person", responses={ 201: 'Returns the newly created person object', 400: 'Was not able to create a new person' },  body=person_fields)
    def post(self) -> Person:
        new_person = Person
        try:
            payload = request.get_json()
            new_person: Person = PersonService.create(payload)
            # raise ValueError('error reised for testing purposes.')
            return new_person, 201
        except Exception as e:
            print('Failed to create a new person: ' + str(e))
            abort(400, "Failed to create a new person")

    @responds(schema=PersonSchema, many=True)
    @api.doc(description = "Return all the person objects", responses={200: 'Returns a list of all the available person objects', 400: 'Was not able to retrieve the person objects'})
    @api.marshal_with(person_fields, as_list=True)
    def get(self) -> List[Person]:
        try: 
            persons: List[Person] = PersonService.retrieve_all()
            return persons
        except Exception as e:
            print('Failed to retrieve the person objects. Details: ' + str(e))
            abort(400, "Failed to retrieve the person objects")
        

@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    @api.doc(description = "Gets the id of a person as parameter and returns the relater person object", responses= { 200: 'Returns a person object based on the given person_id', 404: 'Person not found' })
    @api.marshal_with(person_fields)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        if person is None:
            abort(404, "Person not found")
        return person