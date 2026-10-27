from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from port_checker.checker import check_port


app = Flask(__name__)

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": "http://127.0.0.1:5500"
        }
    }
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def check_port_api():
    data = request.json
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request. Please check your input and try again."}), 400
    host = data.get("host")
    port = data.get("port")
    if not host:
        return jsonify({"error":"Host is required"}), 400

    if not isinstance(port, int) or isinstance(port, bool): 
        return jsonify({"error":"Port must be an integer between 1 and 65535"}), 400

    if not 1 <= port <= 65535:
        return jsonify({"error":"Port must be an integer between 1 and 65535"}), 400

    result = check_port(host, port)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)   