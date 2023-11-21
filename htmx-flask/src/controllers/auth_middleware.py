from functools import wraps
from flask import request, abort, make_response
from src.services.auth_service import AuthService

auth_service = AuthService()

def jwt_required(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'jwt' not in request.cookies:
            abort(401)
        
        try:
            user_id = auth_service.decode_token(request.cookies['jwt'])
        except:
            response = make_response("Unauthorized", 401)
            response.delete_cookie('jwt')
            return response

        return func(user_id, *args, **kwargs)
    
    return wrapper