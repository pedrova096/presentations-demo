from flask import request, redirect, url_for, make_response, render_template
from app import app
from src.models import UserModel
from src.services.user_service import UserRepository
from src.services.auth_service import AuthService
from .auth_middleware import jwt_required
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
        return render_template('partials/kuaatata/single_message.html', message='El email ya existe', error=True), 400
    except Exception as e:
        print(e)
        return redirect(url_for('error')), 500


@app.route("/sign-out", methods=['POST'])
def sign_out():
    response = make_response()
    response.set_cookie('jwt', '', expires=0)
    response.headers['HX-Redirect'] = url_for('kuaatata_sign_up')
    return response, 200


@app.route("/user", methods=['PUT'])
@jwt_required
def update_user(uid):
    form_dict = request.form.to_dict()
    message = ''
    try:
        user = UserModel.from_update_dict(form_dict, uid)
        user_service.update_by(user.to_dict(), id=uid)
        message = render_template(
            'partials/kuaatata/single_message.html', message='Usuario actualizado', success=True)
    except exc.IntegrityError as e:
        print(e)
        message = render_template(
            'partials/kuaatata/single_message.html', message='El email ya existe', error=True)
    except Exception as e:
        print(e)
        return redirect(url_for('error')), 500

    user_initial = user.name[0].upper()
    return render_template('pages/kuaatata/profile.html', user=user, message=message, user_initial=user_initial), 200
