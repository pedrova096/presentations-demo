import os
import json
from fuzzywuzzy import fuzz
from src.repositories.recipe_repository import RecipeRepository

class IngredientsService(object):
    INGREDIENT_EMOJI_JSON = "./constants/ingredients_emoji.json"

    def __init__(self):
        full_path = os.path.join(os.path.dirname(__file__), self.INGREDIENT_EMOJI_JSON)
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
    
class RecipeService(object):
    def __init__(self):
        self.repository = RecipeRepository()
    
    def create(self, entity):
        self.repository.create(entity)
        entity = self.repository.get(entity.id)
        return entity