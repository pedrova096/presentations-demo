from src.repositories.user_repository import UserRepository


class UserService(object):
    def __init__(self):
        self.repository = UserRepository()

    def create(self, entity):
        self.repository.create(entity)
        entity = self.repository.get(entity.id)
        return entity
    
    def get_by_id(self, id):
        return self.repository.get(id)

