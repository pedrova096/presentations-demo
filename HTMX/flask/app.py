from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from routers import actions

db = SQLAlchemy()
main = Blueprint("main", __name__)


def get_nav_page(index):
    pages = ["/part-one", "/part-two", "/part-three", "/part-four"]
    return pages[index - 1] if index > 0 else "#", pages[index + 1] if index < len(pages) - 1 else "#"


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/part-one")
def page_one():
    prev_page, next_page = get_nav_page(0)
    return render_template("pages/part_one.html", next=next_page, prev=prev_page)


@main.route("/part-two")
def part_two():
    prev_page, next_page = get_nav_page(1)
    return render_template("pages/part_two.html", next=next_page, prev=prev_page)


@main.route("/part-three")
def part_three():
    prev_page, next_page = get_nav_page(2)
    return render_template("pages/part_three.html", next=next_page, prev=prev_page)


@main.route("/part-four")
def part_four():
    prev_page, next_page = get_nav_page(3)
    return render_template("pages/part_four.html", next=next_page, prev=prev_page)


def create_app():
    print("Creating app")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(actions.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5050)
