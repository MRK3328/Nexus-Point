import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Flask App
app = Flask(__name__)
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
