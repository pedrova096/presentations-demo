from flask import render_template, request, redirect, url_for
from app import app as views

def get_nav_page(index):
    pages = ["/part-one", "/part-two", "/part-three", "/part-four"]
    return pages[index - 1] if index > 0 else "#", pages[index + 1] if index < len(pages) - 1 else "#"

@views.route("/")
def index():
    return render_template("index.html")


@views.route("/part-one")
def page_one():
    prev_page, next_page = get_nav_page(0)
    return render_template("pages/part_one.html", next=next_page, prev=prev_page)


@views.route("/part-two")
def part_two():
    prev_page, next_page = get_nav_page(1)
    return render_template("pages/part_two.html", next=next_page, prev=prev_page)


@views.route("/part-three")
def part_three():
    prev_page, next_page = get_nav_page(2)
    return render_template("pages/part_three.html", next=next_page, prev=prev_page)


@views.route("/part-four")
def part_four():
    prev_page, next_page = get_nav_page(3)
    return render_template("pages/part_four.html", next=next_page, prev=prev_page)

@views.route("/k")
def kuaatata_page():
    if 'jwt' in request.cookies:
        return redirect(url_for('kuaatata_feed'))
    
    return render_template("pages/kuaatata/sign_up.html")

@views.route("/k/feed")
def kuaatata_feed():
    # return render_template("pages/kuaatata/feed.html")
    return ""

@views.route("/k/add")
def kuaatata_add():
    return render_template("pages/kuaatata/recipe_form.html")

@views.route("/k/profile")
def kuaatata_profile():
    return ""

@views.route("/k/recipe/<int:recipe_id>")
def kuaatata_recipe(recipe_id):
    return ""