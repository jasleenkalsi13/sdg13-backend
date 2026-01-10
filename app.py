from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "status": "running",
        "message": "SDG 13 Climate Action Backend Live"
    }

@app.route("/carbon", methods=["POST"])
def carbon():
    data = request.get_json(force=True)

    transport = data.get("transport", 0)
    electricity = data.get("electricity", 0)
    meat = data.get("meat", 0)

    score = transport + electricity + meat

    if score <= 100:
        level = "Low "
    elif score <= 200:
        level = "Moderate "
    else:
        level = "High "

    return jsonify({
        "carbon_score": score,
        "impact_level": level
    })

if __name__ == "__main__":
    app.run()

