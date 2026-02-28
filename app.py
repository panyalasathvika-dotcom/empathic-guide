from flask import Flask, request, jsonify
from utils import detect_mood, detect_risk
from prompts import RESPONSES, EMERGENCY_MESSAGE

app = Flask(__name__)

@app.route("/")
def home():
    return "Empathic Guide chatbot is running."

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("message", "")

    if detect_risk(user_text):
        return jsonify({"response": EMERGENCY_MESSAGE})

    mood = detect_mood(user_text)
    reply = RESPONSES.get(mood, RESPONSES["neutral"])

    return jsonify({
        "mood": mood,
        "response": reply
    })

app.run(host="0.0.0.0", port=5000)
