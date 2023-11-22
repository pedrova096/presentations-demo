from src.repositories.like_repository import LikeRepository
from src.models.like_model import LikeModel

class LikeService(object):
    def __init__(self):
        self.repository = LikeRepository()

    def like(self, recipe_id, user_id):
        entity = LikeModel.create(recipe_id, user_id)
        self.repository.create(entity)
        return
    
    def dislike(self, recipe_id, user_id):
        entity = self.repository.get_by(recipe_id=recipe_id, user_id=user_id)
        self.repository.delete(entity)
        return
    
    def toggle_like(self, recipe_id, user_id):
        entity = self.repository.get_by(recipe_id=recipe_id, user_id=user_id)

        if entity is None:
            self.like(recipe_id, user_id)
            return 1
        else:
            self.dislike(recipe_id, user_id)
            return -1
        
