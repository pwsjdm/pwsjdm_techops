# techops/error_pages/handlers.py
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    error_title = "404!"
    error_desc = "Error 404: Not found!"
    return render_template('error.html', error_desc=error_desc, error_title=error_title), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    error_title = "403!"
    error_desc = "Error 403: Access Forbidden!"
    return render_template('error.html', error_desc=error_desc, error_title=error_title), 403

@error_pages.app_errorhandler(500)
def error_500(error):
    error_title = "500!"
    error_desc = "Error 500: Internal Server Error!"
    return render_template('error.html', error_desc=error_desc, error_title=error_title), 500