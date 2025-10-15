from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # 🔹 Importante para permitir conexión con React

app = Flask(__name__)
CORS(app)  # 🔹 Esto permite que React (frontend) se conecte al backend

API_KEY = "b1df3a57b8704392c1f8c58446dfcfa5"  # Reemplaza con tu API Key real

@app.route("/clima")
def get_clima():
    ciudad = request.args.get("city")
    if not ciudad:
        return jsonify({"error": "Debe proporcionar una ciudad"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid={API_KEY}&lang=es"
    
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener el clima"}), response.status_code

    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
