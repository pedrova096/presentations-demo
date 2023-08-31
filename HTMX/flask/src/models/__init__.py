from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import *
from .recipe_model import *
from .like_model import *

