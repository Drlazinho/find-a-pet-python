from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler
from src.main.routes.pets_routes import pet_route_bp
from src.main.routes.person_routes import person_route_bp
from src.main.swagger.config import apiSwagger
from src.main.swagger.endpoints_doc import endpoints_ns

#Connect DB
db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)

apiSwagger.init_app(app)
apiSwagger.add_namespace(endpoints_ns)
