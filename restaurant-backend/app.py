from flask import Flask, request, jsonify
from config import Config
from models import db, Customer, Reservation
from flask_cors import CORS
from datetime import datetime
from typing import Dict

from utils import get_available_times

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

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

# Get all reservations
@app.route("/reservations", methods=["GET"])
def get_reservations():
    reservation = Reservation.query.all()
    return jsonify([
        {"id": c.id, "customer": c.customer_id, "date": c.date, "time": str(c.time)}
        for c in reservation
    ])

@app.route("/slots", methods=["GET"])
def get_available_slots():
    try:
        date_param = request.args.get('date')
        date = datetime.now().date()
        full_day_name = None
        if date_param:
            date = datetime.strptime(date_param, "%Y-%m-%d")
            full_day_name = date.strftime("%A")
        available_times = get_available_times(date)       
        if full_day_name and full_day_name.lower() == 'sunday':
            available_times.pop()
            available_times.pop()

        return jsonify({"message": "Reservation slots", "data": (list(available_times))})
    except Exception as e:
        return jsonify({"message": "Internal server error", "error": str(e)}),500

@app.route("/reservations", methods=["POST"])
def create_reservation():  # Changed to singular (one reservation)
    data = request.get_json()
    
    # 1. Validation
    required_fields = ["name", "email", "date", "time", "guests"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"message": f"Missing required field: {field}"}), 400
    
    # Validate email format
    if not "@" in data["email"] or not "." in data["email"]:
        return jsonify({"message": "Invalid email format"}), 400
    
    # Validate date is in the future
    try:
        reservation_date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        if reservation_date < datetime.now().date():
            return jsonify({"message": "Reservation date must be in the future"}), 400
    except ValueError:
        return jsonify({"message": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    try:
        # 2. Find available table for this date/time
        # Check existing reservations for the same date/time
        existing_reservations = Reservation.query.filter_by(
            date=data['date'],
            time=data['time']
        ).all()
        
        # Get tables already booked for this slot
        booked_tables = [r.table_number for r in existing_reservations]
        
        # Find first available table (1-30)
        available_tables = [num for num in range(1, 31) if num not in booked_tables]
        
        if not available_tables:
            return jsonify({"message": "No tables available for this time slot"}), 409
        
        # Use first available table (or random choice)
        table_num = available_tables[0]
        
        # 3. Get customer FIRST
        customer = Customer.query.filter_by(email=data.get('email')).first()
        if not customer:
            customer = Customer(
                full_name=data["name"],
                email=data["email"],
                phone=data.get("phone"),
                news_letter_subscription=data.get("news_letter_subscription", False)  # Your new column
            )
            db.session.add(customer)
            db.session.flush()  # This assigns an ID without committing
        
        # 4. Now create reservation with customer.id
        reservation = Reservation(
            customer_id=customer.id,  # Now this works!
            date=data['date'],
            time=data['time'],
            guests=int(data['guests']),
            special_requests=data.get('specialRequests'),
            status=data.get('status', 'confirmed'),  # Default status
            table_number=table_num
        )
        db.session.add(reservation)
        
        # 5. Commit everything together
        db.session.commit()
        
        return jsonify({
            "message": "Reservation created successfully",
            "reservation_id": reservation.id,
            "customer_id": customer.id,
            "table": table_num
        }), 201
        
    except Exception as e:
        db.session.rollback()
        # Log the error for debugging
        app.logger.error(f"Reservation failed: {str(e)}")
        return jsonify({"message": "Reservation failed", "error": str(e)}), 500

def find_or_create_customer(data: Dict[str, str], db) -> Customer:
    customer = Customer.query.filter_by(email=data.get('email')).first()
    if not customer:
        customer = Customer(
            full_name=data["name"],
            email=data["email"],
            phone=data.get("phone"),
            news_letter_subscription=data.get("news_letter_subscription", False)  # Your new column
        )
        db.session.add(customer)
        db.session.flush()  # This assigns an ID without committing
    return customer

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8002)
