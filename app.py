from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Return a JSON welcome message for the API homepage.
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

# Return all products, optionally filtered by category.
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        normalized_category = category.lower()
        filtered_products = [
            product
            for product in products
            if product["category"].lower() == normalized_category
        ]
        return jsonify(filtered_products), 200

    return jsonify(products), 200

# Return a product by ID, or a JSON 404 response if it does not exist.
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((item for item in products if item["id"] == id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)
