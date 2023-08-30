from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user_model import UserModel

class RecipeModel(BaseModel):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(120), nullable=False)
    description = Column(String(120), nullable=False)
    ingredients = Column(String(120), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(UserModel)
