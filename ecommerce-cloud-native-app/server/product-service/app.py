# app.py for product-service, order-service, and user-service
from flask import Flask

app = Flask(__name__)

@app.route('/product-service/')
def product_service():
    return "Welcome to the Product Service!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
