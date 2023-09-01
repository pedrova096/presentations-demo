from app import sock
from .auth_middleware import jwt_required
from src.services.user_service import UserService
from flask import render_template_string, render_template

users = UserService()

@sock.route('/echo')
@jwt_required
def echo(uid, ws):
    while True:
        try:
            ws.receive()

            _user = users.get_by_id(uid)

            reaction_template = render_template_string("/partials/kuaatata/reactions.html")

            ws.send(reaction_template)
        except Exception as e:
            print(e)
            break