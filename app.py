from flask import Flask, render_template, request, jsonify
import os
from offline_answers import run_command
from llm_handler import ask_ai

app = Flask(__name__)

# Optional: default AI profile
DEFAULT_PROFILE = {"response_style": "simple"}

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")

    # First, try offline commands (includes reminders)
    reply = run_command(user_message)
    if reply:
        return jsonify({"reply": reply})

    # Fallback to AI
    ai_reply = ask_ai(user_message, profile=DEFAULT_PROFILE)
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)