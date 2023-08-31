from flask import render_template, request, make_response, url_for
from app import app
from src.models import RecipeModel
from src.services.recipe_service import IngredientsService, RecipeService
from .auth_middleware import jwt_required

ingredients_service = IngredientsService()
recipe_service = RecipeService()

@app.route("/ingredients/search", methods=["GET"])
def search_ingredients():
    ingredient_query_param = request.args.get("ingredient")

    results = ingredients_service.search(ingredient_query_param)

    return render_template("partials/kauaatata/ingredients_autocomplete.html", ingredients=results)


@app.route("/ingredients", methods=["POST"])
def post_ingredient():
    data = request.form.to_dict()

    if "ingredient" in data and "amount" in data and data["ingredient"] and data["amount"]:
        ingredient = ingredients_service.get_by_name(data["ingredient"])
        return render_template("partials/kauaatata/ingredients_items.html", ingredient={
            "name": data["ingredient"],
            "amount": data["amount"],
            "emoji": ingredient["emoji"] if ingredient else ""
        })

    return None, 401


@app.route("/recipes", methods=["POST"])
@jwt_required
def post_recipe(uid):
    recipe = RecipeModel.from_request_form(request.form, uid)

    recipe = recipe_service.create(recipe)

    recipe_url = url_for("kuaatata_recipe", recipe_id=recipe.id)
    response = make_response()
    response.headers["HX-Redirect"] = recipe_url

    return response, 200

@app.route("/recipes/<int:recipe_id>/like", methods=["POST"])
@jwt_required
def like_recipe(uid, recipe_id):
    recipe_updated = recipe_service.like(recipe_id, uid)
    return render_template("partials/kauaatata/recipe_card.html", recipe=recipe_updated)
