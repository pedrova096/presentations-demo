from src.models import db
from src.controllers import register_controllers
from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

register_controllers()

db.init_app(app)

with app.app_context():
    db.create_all()