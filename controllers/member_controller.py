# controllers/member_controller.py
from flask import Blueprint, request, jsonify
from services.member_service import register, login, UserExistsError

member_bp = Blueprint("member", __name__)

@member_bp.route("/register", methods=["POST"])
def register_route():
    data = request.get_json()
    phone_number = data.get("phoneNumber")
    password = data.get("password")
    if not phone_number or not password:
        return jsonify({"error": "phoneNumber and password are required"}), 400
    try:
        register(phone_number, password)
        return jsonify({"message": "User registered successfully"}), 201
    except UserExistsError:
        return jsonify({"error": "User already exists"}), 409

@member_bp.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    phone_number = data.get("phoneNumber")
    password = data.get("password")
    if not phone_number or not password:
        return jsonify({"error": "phoneNumber and password are required"}), 400
    token = login(phone_number, password)
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401