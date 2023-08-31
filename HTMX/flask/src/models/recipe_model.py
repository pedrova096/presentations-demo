from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user_model import UserModel
import json

class RecipeModel(BaseModel):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(120), nullable=False)
    description = Column(String(120), nullable=True)
    ingredients = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(UserModel)
    like_count = Column(Integer, nullable=True, default=0)

    @staticmethod
    def from_request_form(form, uid):
        ingredients = [json.loads(item) for item in form.getlist("ingredients")]
        ingredients = [[item["name"], item["amount"]] for item in ingredients]
        ingredients = json.dumps(ingredients)
        return RecipeModel(
            title=form.get("title"),
            description=form.get("description"),
            ingredients=ingredients,
            user_id=uid
        )
