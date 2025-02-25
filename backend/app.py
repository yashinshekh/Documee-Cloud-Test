
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    response = {
        'message': 'Hello from Flask API!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
