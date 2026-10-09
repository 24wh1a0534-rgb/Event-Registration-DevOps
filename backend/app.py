from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import re

app = Flask(__name__)
CORS(app)

DATABASE = "registrations.db"

# Create database table
def create_table():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                event TEXT NOT NULL
            )
        """)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    phone = str(data.get("phone", "")).strip()
    event = str(data.get("event", "")).strip()

    if not all([name, email, phone, event]):
        return jsonify({"message": "All fields are required!"}), 400

    if not re.fullmatch(r"\d{10}", phone):
        return jsonify({"message": "Enter a valid 10-digit phone number!"}), 400

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return jsonify({"message": "Enter a valid email address!"}), 400

    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            "INSERT INTO registrations (name, email, phone, event) VALUES (?, ?, ?, ?)",
            (name, email, phone, event)
        )

    return jsonify({"message": "Registration Successful!"}), 201

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Event Registration API is running!"})

if __name__ == "__main__":
    create_table()
    app.run(debug=True, port=5000)