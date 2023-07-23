from flask import Blueprint, request, jsonify, render_template

character_form_bp = Blueprint('character_form', __name__, template_folder='templates')

@character_form_bp.route('/create_character', methods=['GET', 'POST'])
def character_form():
    if request.method == 'GET':
        return render_template('character_form.html', classes=['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard'])
    elif request.method == 'POST':
        data = request.form.to_dict()
        
        if True:
            response = {'status': 'success', 'message': 'Character created successfully.', 'redirect_url': '/'}
            return jsonify(response), 200
        else:
            response = {'status': 'error', 'message': 'Error creating character.'}
            return jsonify(response), 500