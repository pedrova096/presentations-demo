import os
import json
from fuzzywuzzy import fuzz
from src.repositories.recipe_repository import RecipeRepository
from .like_service import LikeService, LikeModel


class IngredientsService(object):
    INGREDIENT_EMOJI_JSON = "./constants/ingredients_emoji.json"

    def __init__(self):
        full_path = os.path.join(os.path.dirname(
            __file__), self.INGREDIENT_EMOJI_JSON)
        self.ingredients = json.load(open(full_path, "r", encoding="utf-8"))

    def search(self, query, threshold=65, limit=3):
        results = []

        if len(query) < 3:
            return results

        for ingredient in self.ingredients:
            name_ratio = fuzz.ratio(query, ingredient["name"])
            id_ratio = fuzz.ratio(query, ingredient["id"])

            if name_ratio >= threshold or id_ratio >= threshold:
                ingredient["ratio"] = max(name_ratio, id_ratio)
                results.append(ingredient)
                if len(results) >= limit:
                    break

        results = sorted(results, key=lambda x: x["ratio"], reverse=True)
        return results

    def get_by_name(self, name):
        for ingredient in self.ingredients:
            if ingredient["name"] == name:
                return ingredient
        return None

    def get_emoji(self, name):
        ingredient = self.get_by_name(name)
        return ingredient["emoji"] if ingredient else ""


class RecipeService(object):
    def __init__(self):
        self.repository = RecipeRepository()
        self.like_service = LikeService()
        self.ingredients_service = IngredientsService()

    def create(self, entity):
        self.repository.create(entity)
        entity = self.repository.get(entity.id)
        return entity

    def like(self, recipe_id, uid):
        recipe = self.repository.get(recipe_id)

        toggle_like = self.like_service.toggle_like(recipe_id, uid)

        recipe.like_count += toggle_like

        self.repository.update(recipe)

        return self.map_feed(recipe, toggle_like == 1)

    def map_feed(self, entity, i_liked=False, ingredients_limit=3):
        try:
            entity.i_liked = i_liked

            ingredients = json.loads(entity.ingredients)
            ingredients = [
                {
                    "name": ingredient[0],
                    "amount": ingredient[1],
                    "emoji": self.ingredients_service.get_emoji(ingredient[0])
                }
                for ingredient in ingredients
            ]

            entity.ingredients = [{"emoji": ingredient["emoji"], "amount": ingredient["amount"], "name": ""}
                                  for ingredient in ingredients if ingredient["emoji"]][:ingredients_limit]

            if len(entity.ingredients) == 0:
                entity.ingredients = [ingredients[0]]

            if len(ingredients) > len(entity.ingredients):
                entity.ingredients.append(
                    {"name": f"+ {len(ingredients) - len(entity.ingredients)} Ing.", "red": True})

        except Exception as e:
            print("Error parsing ingredients", e)
            entity.ingredients = []

        return entity

    def get_all(self, user_id, page_number=1, page_size=10, ingredients_limit=3):
        query = self.repository.get_query_with(LikeModel.id).outerjoin(
            LikeModel, LikeModel.recipe_id == self.repository.model.id and LikeModel.user_id == user_id)

        total_count = query.count()
        entities = query.offset(
            (page_number - 1) * page_size).limit(page_size).all()

        entities = [self.map_feed(entity, bool(like_id), ingredients_limit=ingredients_limit)
                    for entity, like_id in entities]

        return entities, total_count

    def get_all_v2(self, user_id, page_number=1, page_size=10, ingredients_limit=3):
        entities = self.repository.get_query_with(LikeModel.id).outerjoin(
            LikeModel, LikeModel.recipe_id == self.repository.model.id and LikeModel.user_id == user_id).order_by(
                self.repository.model.like_count.desc()).paginate(
                    page=page_number, per_page=page_size, error_out=False)

        entities = [self.map_feed(entity, i_liked=bool(like_id), ingredients_limit=ingredients_limit)
                    for entity, like_id in entities]

        return entities
