from functools import wraps
from flask import request, abort
from src.services.auth_service import AuthService

auth_service = AuthService()

def jwt_required(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'jwt' not in request.cookies:
            abort(401)
        
        try:
            payload = auth_service.decode_token(request.cookies['jwt'])
            user_id = payload['sub']
        except:
            abort(401)
        return func(user_id, *args, **kwargs)
    
    return wrapper