from flask import Blueprint, jsonify
from models import Restaurant

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "Restaurant API"

@main_bp.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name} for r in restaurants])