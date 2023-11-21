from src.models.like_model import LikeModel
from .base import BaseRepository

class LikeRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, LikeModel)
