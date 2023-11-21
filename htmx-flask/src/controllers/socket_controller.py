from app import sock
from .auth_middleware import jwt_required
from src.services.user_service import UserService
from flask import render_template
import random

users = UserService()
rooms = {}

def add_client(room_id, uid, ws):
    rooms[room_id] = rooms.get(room_id, {})
    rooms[room_id][uid] = ws

def send_to_room(room_id, message):
    for uid, client in rooms[room_id].items():
        try:
            client.send(message)
        except:
            client.close()
            remove_close_client(room_id, uid)

def remove_close_client(room_id, uid):
    rooms[room_id].pop(uid, None)

colors=["bg-rose-500", "bg-yellow-500", "bg-cyan-500", "bg-indigo-500",  "bg-violet-500", "bg-teal-500"]
emojis=["fluent-emoji:cook", "fluent-emoji:cook-dark", "fluent-emoji:cook-light", "fluent-emoji:cook-medium",
         "fluent-emoji:woman-cook", "fluent-emoji:woman-cook-dark", "fluent-emoji:woman-cook-light", "fluent-emoji:woman-cook-medium",
         "fluent-emoji:cooking", "fluent-emoji:face-savoring-food", "fluent-emoji:cooking", "fluent-emoji:face-savoring-food"]

@sock.route('/wave/<r_id>', methods=['GET'])
@jwt_required
def wave(uid, ws, r_id):
    
    add_client(r_id, uid, ws)

    while True:
        try:
            ws.receive()

            user_name = users.get_by_id(uid).name
            random_color = random.choice(colors)
            random_emoji = random.choice(emojis)
            reaction_template = render_template("/partials/kuaatata/reactions.html", initial=user_name[0].upper(), color=random_color, emoji=random_emoji)

            send_to_room(r_id, reaction_template)
        except Exception as e:
            print("Exception_socket: ", e)
            if "Connection closed" in str(e):
                remove_close_client(r_id, uid)
                break