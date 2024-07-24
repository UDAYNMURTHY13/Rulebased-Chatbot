import os
from flask import Flask, render_template, request, jsonify
from chatbot import RuleBasedChatbot  # Import your chatbot class from chatbot.py

app = Flask(__name__)

# Get the API key from an environment variable
api_key = 'AIzaSyDbMxR4mc7m4FRMjhSzeK1ZgY9qRhpdaVA'
if not api_key:
    raise ValueError("No API key set for Gemini. Please set the GEMINI_API_KEY environment variable.")

chatbot = RuleBasedChatbot(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    bot_response = chatbot.respond(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)