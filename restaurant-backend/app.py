from flask import Flask, request, jsonify
from config import Config
from models import db, Customer, Reservation

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

# Get all customers
@app.route("/reservations", methods=["GET"])
def get_reservations():
    reservation = Reservation.query
    return jsonify([
        {"id": c.id, "full_name": c.full_name, "email": c.email, "phone": c.phone}
        for c in reservation
    ])

# with app.app_context():
#     db.create_all()
#     print("Database and tables created.")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8002)
