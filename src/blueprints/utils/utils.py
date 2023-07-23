from flask import Blueprint, request, jsonify, render_template
from src.handlers.database import init_database

utils_bp = Blueprint('utils', __name__, template_folder='templates')


@utils_bp.route('/init_db', methods=['GET'])
def init_db():
    try:
        init_database()
        return jsonify({'message': 'Database initialized.'}), 200
    except Exception as e:
        return jsonify({'message': f'Error initializing database: {e}'}), 500