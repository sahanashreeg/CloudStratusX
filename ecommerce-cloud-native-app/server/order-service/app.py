# app.py for product-service, order-service, and user-service
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<service>/')
def home(service):
    return jsonify({"message": f"Welcome to {service}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
