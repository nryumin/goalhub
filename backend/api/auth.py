from flask import request,jsonify,redirect, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from uuid import UUID

from api import api
from app import mongo
from helpers.social import get_facebook_info, get_linkedin_data
from repositories import UserRepository, get_frontend_data
from helpers.mail import sendMail
from helpers.exceptions import UserAlreadyExists


@api.route("/login", methods=["POST"])
def login():
    if request.json['login_type'] == 'email':
        email = request.json['email']
        user = UserRepository.get_by_email(email)
        if not user or not check_password_hash(user.password_hash, request.json['password']):
            return jsonify({'success': False, 'message': 'Bad login/password'})
        if not user.confirmed:
            return jsonify({'success': False, 'message': 'User not confirmed'})
        login_user(user, remember=True)
    elif request.json['login_type'] == 'fb':
        start_with_fb(request.json['token'])
    elif request.json['login_type'] == 'linkedin':
        start_with_linkedin(request.json)

    return jsonify({'success': True, 'data': get_frontend_data()})


@api.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True})


@api.route("/register", methods=["POST"])
def register():
    if request.json['registration_type'] == 'email' or request.json['type'] == 'employer':
        token = uuid4()
        user = {
            'email': request.json['email'],
            'password_hash': generate_password_hash(request.json['password']),
            'type': request.json['type'],
            'confirmed': False,
            'confirm_token': token,
        }

        if request.json['type'] == 'employee':
            user['first_name'] = request.json['first_name']
            user['last_name'] = request.json['last_name']
        else:
            user['name'] = request.json['name']
            user['positions'] = []

        UserRepository.insert(user)

        receiver = request.json['email']
        subject = u'PITCH ME:Confirm registration'
        text = u'Follow link to <a href="{}api/confirm?token={}">finish registration</a>'.format(request.host_url, token)
        sendMail(receiver, subject, text)
        return jsonify({'success': True})
    elif request.json['registration_type'] == 'fb':
        try:
            user = start_with_fb(request.json['token'])
        except UserAlreadyExists:
            return jsonify({'success': False, 'message': 'User with your email already exist. Login using your email.'})

        return jsonify({'success': True, 'user': user.get_dto()})
    elif request.json['registration_type'] == 'linkedin':
        try:
            user = start_with_linkedin(request.json)
        except UserAlreadyExists:
            return jsonify({'success': False, 'message': 'User with your email already exist. Login using your email.'})

        return jsonify({'success': True, 'user': user.get_dto()})


def start_with_fb(token):
    user_data = get_facebook_info(token)

    user = UserRepository.get_by_email(user_data['email'])

    if user and 'facebook' not in user.external_accounts:
        raise UserAlreadyExists()

    if not user:
        user_data['type'] = 'employee'
        user_data['confirmed'] = True
        user = UserRepository.insert(user_data)

    login_user(user, remember=True)


def start_with_linkedin(data):
    user_data = get_linkedin_data(data)

    user = UserRepository.get_by_email(user_data['email'])

    if user and 'linkedin' not in user.external_accounts:
        raise UserAlreadyExists()

    if not user:
        user_data['type'] = 'employee'
        user_data['confirmed'] = True
        user = UserRepository.insert(user_data)

    login_user(user, remember=True)


@api.route("/check-email", methods=["POST"])
def check_email():
    valid = not UserRepository.get_by_email({'email': request.json['email']})
    return jsonify({'valid': valid})


@api.route("/confirm", methods=["GET"])
def confirm():
    token = request.args.get('token')
    if not token:
        return redirect("/")

    user = UserRepository.get_by_token(UUID(token))
    if not user:
        flash(u'Bad token', 'error')
        return redirect("/")

    user = UserRepository.update({'confirm_token': UUID(token)},
                                 {'$set': {'confirmed': True}, '$unset': {'confirm_token': ''}},)
    login_user(user, remember=True)

    receiver = user.email
    subject = u'PITCH ME:Registration completed'
    text = u'Welcome to PitchMe, thank you for completing your registration. We can help you with…'
    sendMail(receiver, subject, text)
    return redirect("/")

import smtplib
from email.mime.text import MIMEText

@api.route("/test", methods=["GET"])
def test():
    r.r = "regege"
    return "Success"
