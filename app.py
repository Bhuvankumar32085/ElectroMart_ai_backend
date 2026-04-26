import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# load env variables
load_dotenv()

# import AI service
from services.ai_service import get_ai_response

app = Flask(__name__)

# CORS setup (important for Next.js frontend)
CORS(
    app,
    resources={r"/*": {"origins": os.getenv("NEXT_API_BASE")}},  # production me specific domain lagana
    supports_credentials=True
)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({
        "success": True,
        "message": "Pong! Server is running."
    })
    
    
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        message = data.get("message")
        user_id = data.get("userId")

        if not message:
            return jsonify({"error": "Message required"}), 400

        reply = get_ai_response(message, user_id)

        return jsonify({
            "success": True,
            "reply": reply
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Internal Server Error"}), 500

    

# Run server
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5012))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
