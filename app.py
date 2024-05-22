# app.py

from flask import Flask, jsonify
from routes import api
from config import USERNAME
from flask_cors import CORS, cross_origin # need when deploy on server 
from waitress import serve

app = Flask(__name__) 
CORS(app)

# Load the configuration from the config.py file
app.config.from_pyfile('config.py')
# Register the API blueprint
app.register_blueprint(api)
app.config['SECRET_KEY'] = 'your_secret_key_here'


# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Page not found", "status_code": 404}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error", "status_code": 500}), 500
# You can add more app configurations here if needed

if __name__ == '__main__':
    app.run(debug=False)
        # serve(app, host="0.0.0.0", port=8080)
