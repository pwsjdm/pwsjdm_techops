# techops/__init__.py
from flask import Flask

app = Flask(__name__)

from techops.core.views import core
app.register_blueprint(core)