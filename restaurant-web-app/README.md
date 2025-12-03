[preview here](https://quantico-bistro.netlify.app/)


<!-- 
===========================================
BACKEND IMPLEMENTATION GUIDE
===========================================

NODEJS/EXPRESS EXAMPLE:

// File: server.js or routes/newsletter.js

const express = require('express');
const router = express.Router();
const { body, validationResult } = require('express-validator');

// Database model (MongoDB/Mongoose example)
const Newsletter = require('../models/Newsletter');

// POST /api/newsletter/subscribe
router.post(
  '/subscribe',
  [
    body('email').isEmail().normalizeEmail(),
    body('name').trim().notEmpty(),
  ],
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const { email, name, subscribedAt } = req.body;

      // Check if email already exists
      const existing = await Newsletter.findOne({ email });
      if (existing) {
        return res.status(409).json({
          message: 'This email is already subscribed',
        });
      }

      // Create new subscriber
      const subscriber = new Newsletter({
        email,
        name,
        subscribedAt: subscribedAt || new Date(),
        isActive: true,
      });

      await subscriber.save();

      res.status(201).json({
        message: 'Successfully subscribed',
        subscriber: {
          id: subscriber._id,
          email: subscriber.email,
        },
      });
    } catch (error) {
      console.error('Newsletter error:', error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }
);

module.exports = router;

===========================================
DATABASE SCHEMA (MongoDB)
===========================================

const mongoose = require('mongoose');

const newsletterSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true,
  },
  name: {
    type: String,
    required: true,
    trim: true,
  },
  subscribedAt: {
    type: Date,
    default: Date.now,
  },
  isActive: {
    type: Boolean,
    default: true,
  },
}, { timestamps: true });

module.exports = mongoose.model('Newsletter', newsletterSchema);

===========================================
SQL DATABASE SCHEMA
===========================================

CREATE TABLE newsletter_subscribers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_email (email),
  INDEX idx_is_active (is_active)
);

 -->