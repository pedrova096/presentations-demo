from flask import Blueprint, request, render_template
from datetime import datetime
from time import sleep
import locale

bp = Blueprint("actions", __name__)


@bp.route("/image")
def image():
    return render_template("/partials/sections/swap.html")


@bp.route("/clock-time")
def clock_time():
    time = datetime.now()
    locale.setlocale(locale.LC_ALL, "es_ES")
    month = time.strftime("%b").capitalize()
    week_day = time.strftime("%A").capitalize()
    return render_template("/partials/sections/swap_next.html", hour=time.hour, minute=time.minute, day=time.day, month=month, week_day=week_day)


@bp.route("/message", methods=["POST"])
def message():
    message = request.form.get("message")
    return render_template("/partials/sections/post_message.html", message=message)


@bp.route("/message/slow", methods=["POST"])
def message_slow():
    message = request.form.get("message")
    sleep(1.5)
    return render_template("/partials/sections/post_message.html", message=message)
