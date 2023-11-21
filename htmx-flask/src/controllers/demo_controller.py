from flask import request, render_template
from app import app
from datetime import datetime
from time import sleep
import locale

@app.route("/image")
def image():
    return render_template("/partials/demo/swap.html")

@app.route("/clock-time")
def clock_time():
    time = datetime.now()
    locale.setlocale(locale.LC_ALL, "es_ES")
    month = time.strftime("%b").capitalize()
    week_day = time.strftime("%A").capitalize()
    return render_template("/partials/demo/swap_next.html", hour=time.hour, minute=time.minute, day=time.day, month=month, week_day=week_day)


@app.route("/message", methods=["POST"])
def message():
    message = request.form.get("message")
    return render_template("/partials/demo/post_message.html", message=message)


@app.route("/message/slow", methods=["POST"])
def message_slow():
    message = request.form.get("message")
    sleep(1.0)
    return render_template("/partials/demo/post_message.html", message=message)
