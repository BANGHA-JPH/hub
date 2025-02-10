from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import logging

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Allow frontend to communicate with backend

# Configure logging to write login attempts to a file
logging.basicConfig(filename='login_attempts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Dummy user database (Replace with real database in production)
users = {
    "user@example.com": bcrypt.generate_password_hash("password123").decode('utf-8')
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Log the login attempt
    logging.info(f"Login attempt - Username: {username}, Password: {password}")

    if username in users and bcrypt.check_password_hash(users[username], password):
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid credentials", "status": "error"}), 401

if __name__ == '__main__':
    app.run(debug=True)
