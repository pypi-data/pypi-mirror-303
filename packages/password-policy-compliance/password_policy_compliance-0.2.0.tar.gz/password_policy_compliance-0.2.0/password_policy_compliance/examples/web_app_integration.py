from flask import Flask, request, jsonify
from password_policy_compliance import (
    password_validator,
    policy_compliance,
    password_strength,
)

app = Flask(__name__)

# In a real application, you would store this securely, not as a global variable
user_database = {}

# Use PCI DSS policy for this example
policy = policy_compliance.get_policy("PCI_DSS")

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    validation_result = password_validator.validate_password(password, policy)
    if not validation_result["valid"]:
        return jsonify({
            "error": "Password does not meet policy requirements",
            "details": validation_result["errors"]
        }), 400

    strength_result = password_strength.calculate_password_strength(password)
    if strength_result["score"] < 70:
        return jsonify({
            "error": "Password is too weak",
            "strength_score": strength_result["score"],
            "feedback": strength_result["feedback"]
        }), 400

    user_database[username] = password
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username not in user_database or user_database[username] != password:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200

@app.route('/password_strength', methods=['POST'])
def check_password_strength():
    password = request.json.get('password')

    if not password:
        return jsonify({"error": "Password is required"}), 400

    strength_result = password_strength.calculate_password_strength(password)
    crack_time = password_strength.get_crack_time_estimation(password)

    return jsonify({
        "strength_score": strength_result["score"],
        "feedback": strength_result["feedback"],
        "crack_times": crack_time["crack_times_display"]
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
