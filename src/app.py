from flask import Flask, jsonify
from src.blueprints.character_form.character_form import character_form_bp
from src.blueprints.utils.utils import utils_bp

app = Flask(__name__)

app.register_blueprint(character_form_bp)
app.register_blueprint(utils_bp)
