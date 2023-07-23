from flask import Blueprint, request, jsonify, render_template

character_form_bp = Blueprint('character_form', __name__, template_folder='templates')

@character_form_bp.route('/create_character', methods=['GET', 'POST'])
def character_form():
    if request.method == 'GET':
        return render_template('character_form.html')