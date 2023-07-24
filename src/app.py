from flask import Flask, jsonify
from src.blueprints.character_form.character_form import character_form_bp
from src.blueprints.utils.utils import utils_bp
from src.blueprints.home.home import home_bp
from src.blueprints.show_characters.show_characters import show_characters_bp

app = Flask(__name__)

app.register_blueprint(character_form_bp)
app.register_blueprint(utils_bp)
app.register_blueprint(home_bp)
app.register_blueprint(show_characters_bp)
