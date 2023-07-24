from flask import Blueprint, render_template, redirect, request, jsonify
from src.handlers.show_characters import get_characters
from src.handlers.write_character import update_character_in_db
from src.models.character import Character, Attributes, Skills, Perks
import json
import logging


show_characters_bp = Blueprint('show_characters', __name__, template_folder='templates')


@show_characters_bp.route('/show_characters')
def show_characters():
    characters = get_characters()
    characters = [character.to_dict() for character in characters]
    return render_template('show_characters.html', characters_data=characters)


@show_characters_bp.route('/show_characters/<string:name>')
def view_character(name):
    characters = get_characters()
    for character in characters:
        if character.name == name:
            character = character.to_dict()
            return render_template('view_character.html', character=character)
    return redirect('/show_characters')


@show_characters_bp.route('/edit_character/<string:name>')
def edit_character(name):
    characters = get_characters()
    for character in characters:
        if character.name == name:
            character = character.to_dict()
            return render_template('edit_character.html', character=character)
    return redirect('/show_characters')



@show_characters_bp.route('/update_character', methods=['POST'])
def update_character():
    logging.info(f"update_character called")
    
    character_data = request.form.to_dict()
    print(character_data)
    
    character = Character(
        id=character_data['id'],
        name=character_data['name'],
        level=character_data['level'],
        experience=character_data['experience'],
        origin=character_data['origin'],
        attributes=Attributes(
            strength=character_data['strength'],
            perception=character_data['perception'],
            endurance=character_data['endurance'],
            charisma=character_data['charisma'],
            intelligence=character_data['intelligence'],
            agility=character_data['agility'],
            luck=character_data['luck']
        ),
        skills=[
            Skills(
                id=skill_data['id'],  # Add the skill_id if available
                skill=skill_data['skill'],
                attribute=skill_data['attribute'],
                details=skill_data['details']
            )
            for skill_data in json.loads(character_data['skills'].replace("'", '"').removeprefix('"').removesuffix('"'))
        ] or [],
        perks=[
            Perks(
                id=perk_data.get('id'),  # Add the perk_id if available
                name=perk_data['name'],
                rank=perk_data['rank'],
                description=perk_data['description']
            )
            for perk_data in json.loads(character_data['perks'].replace("'", '"').removeprefix('"').removesuffix('"'))
        ] or []
    )
    
    logging.info(f"character is {character}")
    
    edit_character_response = update_character_in_db(character)
    print('-------------------')
    print(edit_character_response)
    print('-------------------')
    
    if edit_character_response:
        response = {
            'status': 'success',
            'message': 'Character updated successfully',
            'redirect_url': '/show_characters'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 'error',
            'message': 'Error updating character',
            'redirect_url': '/show_characters'
        }
        return jsonify(response), 500
        

                        