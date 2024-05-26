from flask_restx import fields
from .config import apiSwagger

person_models = apiSwagger.model('Person', {
    "first_name": fields.String,
    "last_name": fields.String,
    "age": fields.Integer,
    "pet_id": fields.Integer,
})
