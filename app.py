from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(_name_)
CORS(app)  

@app.route("/")
def home():
    return {
        "status": "running",
        "message": "SDG 13 Climate Action Backend Live "
    }

@app.route("/carbon", methods=["POST"])
def carbon():
    data = request.json
    score = sum(data.values())

    if score <= 4:
        level = "Low"
    elif score <= 8:
        level = "Moderate"
    else:
        level = "High"

    return jsonify({
        "carbon_score": score,
        "impact_level": level
    })

if _name_ == "_main_":
    app.run()
