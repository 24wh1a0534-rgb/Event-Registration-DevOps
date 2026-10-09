
# Event Registration System

DevOps Experiment 1 - Event Registration using Flask Microframework

Roll Number: 24WH1A0534

## Technologies
- HTML
- CSS
- JavaScript
- Python Flask
- SQLite
- REST API

## Features
- Event registration form
- Form validation
- Backend API
- SQLite database storage
- Registration success message

## Run Backend

cd backend
python -m pip install -r requirements.txt
python app.py

## Run Frontend

cd frontend
python -m http.server 5500

Open http://localhost:5500

## API Endpoint

POST /register

Example JSON:

{
  "name": "Test Student",
  "email": "test@example.com",
  "phone": "9876543210",
  "event": "Hackathon"
}
