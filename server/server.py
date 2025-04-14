from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

util.load_saved_artifacts()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_location_names")
def get_location_names():
    res = jsonify({
        "locations": util.get_location_names()
    })
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

@app.route("/predict_home_price",methods=["POST"])
def predict_home_price():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    sqft = float(data["total_sqft"])
    location = data["location"]
    bhk = int(data["bhk"])
    bath = int(data["bath"])

    response = jsonify({
        "estimated_price": util.get_estimated_price(location, sqft, bhk, bath)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run()