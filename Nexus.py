import os
import openai
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS  # Import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Flask App
app = Flask(__name__, template_folder="templates")  # Ensure templates folder is used
CORS(app)  # Enable CORS for all routes

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Function to process AI responses
def process_ai_command(command):
    if "hello" in command.lower():
        return "Hello! How can I assist you today?"
    elif "who are you" in command.lower():
        return "I am your Nexus AI Assistant!"
    else:
        return "I didn't understand that. Can you try again?"

# Route to serve the login page
@app.route('/')
def login():
    return render_template("index_login.html")  # Load the login page first

# Route to handle login
@app.route('/login', methods=['POST'])
def handle_login():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")

    # Check credentials (for now, hardcoding as "jk33" and "3328")
    if username == "jk33" and password == "3328":
        return jsonify({"redirect": url_for('dashboard')})  # Redirect to the main dashboard
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Route to serve the CEO dashboard
@app.route('/dashboard')
def dashboard():
    return render_template("index.html")  # Load the main dashboard after login

# Route to handle voice commands
@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get("command", "")

    if not command:
        return jsonify({"message": "No command received"}), 400

    ai_response = process_ai_command(command)
    return jsonify({"message": ai_response})

# Run the Flask app for deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Adjusted for Render deployment
