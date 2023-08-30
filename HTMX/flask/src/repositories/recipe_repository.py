from src.models.recipe_model import RecipeModel
from .base import BaseRepository

class RecipeRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, RecipeModel)
