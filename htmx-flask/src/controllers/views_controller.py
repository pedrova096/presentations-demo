from flask import render_template, request, redirect, url_for, make_response
from app import app as views
from .auth_middleware import jwt_required
from src.services.recipe_service import RecipeService
from src.services.user_service import UserService

recipe_service = RecipeService()
user_service = UserService()


def get_nav_page(index):
    pages = ["/part-one", "/part-two", "/part-three", "/part-four"]
    return pages[index - 1] if index > 0 else "#", pages[index + 1] if index < len(pages) - 1 else "#"


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/part-one")
def part_one():
    prev_page, next_page = get_nav_page(0)
    return render_template("pages/demo/part_one.html", next=next_page, prev=prev_page)


@views.route("/part-two")
def part_two():
    prev_page, next_page = get_nav_page(1)
    return render_template("pages/demo/part_two.html", next=next_page, prev=prev_page)


@views.route("/part-three")
def part_three():
    prev_page, next_page = get_nav_page(2)
    return render_template("pages/demo/part_three.html", next=next_page, prev=prev_page)


@views.route("/part-four")
def part_four():
    prev_page, next_page = get_nav_page(3)
    return render_template("pages/demo/part_four.html", next=next_page, prev=prev_page)


@views.route("/k/sign-up")
def kuaatata_sign_up():
    if 'jwt' in request.cookies:
        return redirect(url_for('kuaatata_feed'))

    return render_template("pages/kuaatata/sign_up.html")


@views.route("/k/feed")
@jwt_required
def kuaatata_feed(uid):
    page_number = request.args.get("page_number", 1, type=int)
    recipes, pagination = recipe_service.get_all(
        user_id=uid, page_size=5, page_number=page_number)
    return render_template("pages/kuaatata/recipe_feed.html", recipes=recipes, pagination=pagination)


@views.route("/k/share")
@jwt_required
def kuaatata_share(_uid):
    return render_template("pages/kuaatata/recipe_form.html")


@views.route("/k/profile")
@jwt_required
def kuaatata_profile(uid):
    user = user_service.get_by_id(uid)
    user.phone = int(user.phone)
    user_initial = user.name[0].upper()
    return render_template("pages/kuaatata/profile.html", user=user, user_initial=user_initial)


@views.route("/k/recipe/<int:recipe_id>")
@jwt_required
def kuaatata_recipe(uid, recipe_id):
    recipe = recipe_service.get_by_id(recipe_id)
    return render_template("pages/kuaatata/recipe_detail.html", recipe=recipe)


@views.route("/k/loading")
def kuaatata_loading():
    return render_template("pages/kuaatata/loading.html")


@views.route("/k/redirection")
def kuaatata_redirection():
    response = make_response()
    response.headers['HX-Redirect'] = url_for('kuaatata_sign_up')
    return response, 200
