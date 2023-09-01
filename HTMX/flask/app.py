from src.models import db
from src.controllers import register_controllers
from flask import Flask
from flask_sock import Sock

app = Flask(__name__)

app.config.from_object('config')

sock = Sock(app)

db.init_app(app)
sock.init_app(app)

register_controllers()

# with app.app_context():
#     db.create_all()
#     # import sqlite3
#     # connection = sqlite3.connect('database.db')
#     # cursor = connection.cursor()
#     # with open('src/seed/recepies.sql') as f:
#     #     cursor.executescript(f.read())
#     #     connection.commit()
#     #     cursor.close()
#     #     connection.close()
