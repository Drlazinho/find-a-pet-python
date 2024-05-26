from flask_restx import Resource, Namespace

from src.main.routes.person_routes import create_person, find_person
from src.main.routes.pets_routes import delete_pet, list_pets
from .model import person_models

endpoints_ns = Namespace(name='api', description='Api endpoints')

@endpoints_ns.route("/people")
class CreatePerson(Resource):
    @endpoints_ns.expect(person_models)
    def post(self):
        create_person()

@endpoints_ns.route('/people/<person_id>')
class GetPersonID(Resource):
    def get(self, person_id):
        find_person(person_id)

@endpoints_ns.route("/pets")
class GetPets(Resource):
    def get(self):
        list_pets()

@endpoints_ns.route("/pets/<name>")
class DeletePets(Resource):
    def delete(self, name):
        delete_pet(name)
