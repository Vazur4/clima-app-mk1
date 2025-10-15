from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)
API_KEY = "TuApiKeu"
@app.route("/clima")
def get_clima():
    ciudad = request.args.get("city")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid={API_KEY}"
    response = request.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug = True)