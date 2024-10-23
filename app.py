from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 200,
        'message': 'Welcome to Calculator API',
        'operations_available': ['add', 'subtract', 'multiply', 'divide'],
        'usage': 'Use format: /operation/numberA/numberB'
    })

@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    result = num1 + num2
    return jsonify({'status': 200, 'result': result})

@app.route('/minus/<float:num1>/<float:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return jsonify({'status': 200, 'result': result})

@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return jsonify({'status': 200, 'result': result})

@app.route('/divide/<float:num1>/<float:num2>')
def divide(num1, num2):
    if num2 == 0:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed'}), 400
    result = num1 / num2
    return jsonify({'status': 200, 'result': result})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 404, 'error': 'Not found'}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'status': 400, 'error': 'Bad request - invalid numbers provided'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

