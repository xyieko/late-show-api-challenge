from flask import Blueprint, jsonify
from ..models.guest import Guest

guest_bp = Blueprint("guest", __name__)

@guest_bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    result = [
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        } for guest in guests
    ]
    return jsonify(result), 200