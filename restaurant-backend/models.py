from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    reservations = relationship("Reservation", back_populates="customer")

    def __repr__(self):
        return f"<Customer {self.full_name}>"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    

from sqlalchemy import Integer, String, DateTime, Text, Date, Time, ForeignKey
from sqlalchemy.sql import func
# from datetime import datetime

# Base = declarative_base()

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(Integer, primary_key=True, index=True)
    customer_id =  db.Column(Integer, ForeignKey("customers.id"), nullable=False)
    # Date and time - store separately or combined
    date =  db.Column(Date, nullable=False)  # For date part only
    time =  db.Column(Time, nullable=False)   # For time part only

    guests =  db.Column(Integer, nullable=False, default=2)
    special_requests =  db.Column(Text, nullable=True)
    
    # Additional useful fields
    status =  db.Column(String(20), default='pending')  # pending, confirmed, cancelled, completed
    created_at =  db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at =  db.Column(DateTime(timezone=True), onupdate=func.now())
    
    # Optional fields you might want
    table_number =  db.Column(Integer, nullable=True)
    duration_minutes =  db.Column(Integer, default=90)  # Default reservation duration
    reservation_code =  db.Column(String(10), unique=True, nullable=True)  # For customer reference
    
    def __repr__(self):
        return f"<Reservation(id={self.id}, name={self.name}, date={self.date}, time={self.time}, guests={self.guests})>"