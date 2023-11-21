from src.models.recipe_model import RecipeModel
from src.models.like_model import LikeModel
from .base import BaseRepository
from sqlalchemy import and_

class RecipeRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, RecipeModel)

    def get_with_like_by_uid(self, user_id, page_number=1, page_size=10):
        query = self.get_query_with(LikeModel.id).outerjoin(
            LikeModel, and_(LikeModel.recipe_id == self.model.id, LikeModel.user_id == user_id)
        ).order_by(self.model.like_count.desc())

        recipes = query.paginate(page=page_number, per_page=page_size, error_out=False)

        pagination = { "page": recipes.page, "pages": recipes.pages, "total": recipes.total, "has_next": recipes.has_next, "next_num": recipes.next_num }

        return recipes.items, pagination

    
