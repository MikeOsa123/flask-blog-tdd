from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify
from flask_login import current_user, login_required
from app import db
from app.blog.forms import EditProfileForm, EmptyForm, PostForm
from app.models import User, Post, Comments
from app.translate import translate
from app.main import bp