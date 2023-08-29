from flask import request
from app import app
from src.models import UserModel
from src.services.user_service import UserRepository

user_service = UserRepository()

@app.route("/sign-up", methods=['POST'])
def post():
    form_dict = request.get_json()
    try:
        user = UserModel.from_dict(form_dict)
        user = user_service.create(user)
        return "OK"
    except Exception as e:
        return "NOT_OK"
