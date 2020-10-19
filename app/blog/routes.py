from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify
from flask_login import current_user, login_required

from app.blog import bp
from app import db

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return "Hello, World!"