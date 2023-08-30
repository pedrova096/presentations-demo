from flask import request, redirect, url_for, make_response, render_template
from app import app
from src.models import UserModel
from src.services.user_service import UserRepository
from src.services.auth_service import AuthService
from sqlalchemy import exc

user_service = UserRepository()
auth_service = AuthService()

@app.route("/sign-up", methods=['POST'])
def post():
    form_dict = request.form.to_dict()
    try:
        user = UserModel.from_dict(form_dict)
        user = user_service.create(user)

        atoken = auth_service.create_access_token(user.id)
        
        feed_url = url_for('kuaatata_feed')
        response = make_response()
        response.set_cookie('jwt', atoken)
        response.headers['HX-Redirect'] = feed_url

        return response, 200
    except exc.IntegrityError as e:
        return render_template('partials/kauaatata/single_error.html', error='El email ya existe'), 400
    except Exception as e:
        print(e)
        return redirect(url_for('error')), 500