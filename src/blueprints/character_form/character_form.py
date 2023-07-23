from flask import Blueprint, request, jsonify, render_template
from src.models.character import Character, Attributes, Skills, Perks
from src.handlers.write_character import create_new_character

character_form_bp = Blueprint('character_form', __name__, template_folder='templates')

@character_form_bp.route('/create_character', methods=['GET', 'POST'])
def character_form():
    if request.method == 'GET':
        return render_template('character_form.html', 
                               origins=['Wastelander', 'Vault Dweller', 'Raider', 'Brotherhood of Steel', 'Enclave', 'Super Mutant', 'Ghoul', 'Robot', 'Alien', 'Human'],
                               )
    elif request.method == 'POST':
        data = request.form.to_dict()
        character = Character(**data)
        
        if create_new_character(character):
            response = {'status': 'success', 'message': 'Character created successfully.', 'redirect_url': '/'}
            return jsonify(response), 200
        else:
            response = {'status': 'error', 'message': 'Error creating character.'}
            return jsonify(response), 500