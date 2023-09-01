from app import sock
from .auth_middleware import jwt_required
from src.services.user_service import UserService
from flask import render_template
import random

users = UserService()
clients_ws = []

colors=["bg-rose-500", "bg-yellow-500", "bg-cyan-500", "bg-indigo-500",  "bg-violet-500", "bg-teal-500"]
emojis=["fluent-emoji:cook", "fluent-emoji:cook-dark", "fluent-emoji:cook-light", "fluent-emoji:cook-medium",
         "fluent-emoji:woman-cook", "fluent-emoji:woman-cook-dark", "fluent-emoji:woman-cook-light", "fluent-emoji:woman-cook-medium",
         "fluent-emoji:cooking", "fluent-emoji:face-savoring-food", "fluent-emoji:cooking", "fluent-emoji:face-savoring-food"]

def remove_client_by_uid(uid):
    for client in clients_ws:
        if client[0] == uid:
            clients_ws.remove(client)
            break

@sock.route('/echo')
@jwt_required
def echo(uid, ws):
    clients_ws.append((uid, ws))

    while True:
        try:
            ws.receive()

            user_name = users.get_by_id(uid).name
            random_color = random.choice(colors)
            random_emoji = random.choice(emojis)
            reaction_template = render_template("/partials/kuaatata/reactions.html", initial=user_name[0].upper(), color=random_color, emoji=random_emoji)

            for _, client in clients_ws:
                try:
                    client.send(reaction_template)
                except:
                    remove_client_by_uid(uid)

        except Exception as e:
            if "Connection closed" in str(e):
                remove_client_by_uid(uid)
                break