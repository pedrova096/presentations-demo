from src.models.user_model import UserModel
from .base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, UserModel)
