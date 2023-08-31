from src.models import db


class BaseRepository(object):
    def __init__(self, model):
        """
        Initialize the repository object
        """
        self.model = model

    def get(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        return entity
    
    def get_by(self, **kwargs):
        entity = db.session.query(self.model).filter_by(**kwargs).first()
        return entity

    def get_all(self):
        entities = db.session.query(self.model).all()
        return entities

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()

    def update(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def get_query_with(self, *args):
        try:
            return db.session.query(self.model, *args)
        finally:
            db.session.close()