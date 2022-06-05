# techops/core/views.py
from flask import render_template, request, Blueprint, url_for

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')