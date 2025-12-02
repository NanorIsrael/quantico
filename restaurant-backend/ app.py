from flask import Flask, request, jsonify
from config import Config
from models import db, Customer

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    return {"message": "Flask + PostgreSQL is running!"}

# Create a new customer
@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.json
    customer = Customer(
        full_name=data["full_name"],
        email=data["email"],
        phone=data.get("phone")
    )
    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Customer created", "customer_id": customer.id})

# Get all customers
@app.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    return jsonify([
        {"id": c.id, "full_name": c.full_name, "email": c.email, "phone": c.phone}
        for c in customers
    ])

if __name__ == "__main__":
    app.run(debug=True)
