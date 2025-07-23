import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Routes
@app.route('/')
def home():
    logger.info("Root route accessed")
    return jsonify({
        "status": "success",
        "message": "CloudTrackr backend is running!"
    })

@app.route('/health')
def health_check():
    logger.info("Health check route accessed")
    return jsonify({"health": "ok"})

# Custom error handlers
@app.errorhandler(404)
def not_found(error):
    logger.warning("404 Not Found: %s", error)
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error("500 Internal Server Error: %s", error)
    return jsonify({"error": "Internal server error"}), 500

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
