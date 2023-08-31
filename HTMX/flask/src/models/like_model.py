from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user_model import UserModel
from .recipe_model import RecipeModel
import json

class LikeModel(BaseModel):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    user = relationship(UserModel)
    recipe = relationship(RecipeModel)

    @staticmethod
    def create(recipe_id, uid):
        return LikeModel(
            user_id=uid,
            recipe_id=recipe_id
        )
