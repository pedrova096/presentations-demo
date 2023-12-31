import bcrypt
from sqlalchemy import Column, Integer, String, Numeric
from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(Numeric(120), nullable=False)
    password_hash = Column(String(128), nullable=False)

    @staticmethod
    def from_dict(req_dict):
        password_hash = bcrypt.hashpw(req_dict.get(
            'password').encode('utf-8'), bcrypt.gensalt())
        password_hash = password_hash.decode('utf-8')
        return UserModel(
            name=req_dict.get('name'),
            email=req_dict.get('email'),
            phone=req_dict.get('phone'),
            password_hash=password_hash
        )

    @staticmethod
    def from_update_dict(req_dict, uid):
        return UserModel(
            id=uid,
            name=req_dict.get('name'),
            email=req_dict.get('email'),
            phone=req_dict.get('phone')
        )

    def to_dict(self):
        return {
            # and value != None and no id
            c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id' and getattr(self, c.name) != None
        }
