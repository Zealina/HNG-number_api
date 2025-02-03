#!/usr/bin/env python3
"""
Number classification API
"""

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from typing import List
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Index Page"""
    result = {"text": "Welcome to Zealina\'s Number Classification API",
              "usage": "https://zealina-number-api.onrender.com/api/classify-number?number=<number>"}
    return (jsonify(result)), 200


@app.route('/api/classify-number')
def classify_number():
    """Return the properties and fun facts of the number"""
    if len(request.args) > 1 or request.args.get('number') == None:
        abort(400)
    try:
        value = int(request.args['number'])
    except ValueError:
        abort(400)
    result = {
            'number': value,
            'is_prime': is_prime(value),
            'is_perfect': is_perfect(value),
            'properties': properties(value),
            'digit_sum': digit_sum(value),
            'fun_fact': fun_fact(value)
            }
    return (jsonify(result)), 200


@app.errorhandler(400)
def bad_request(e):
    """Return Invalid Request Json"""
    value = {'number': 'alphabet', 'error': True}
    return (jsonify(value)), 400


def is_prime(value :int) -> bool:
    """Check if value is prime"""
    if value < 2 or value % 2 == 0 and value != 2:
        return False
    if value < 9:
        return True
    for test in range(3, int(value ** 0.5) + 1, 2):
        if value % test == 0:
            return False
    return True


def is_perfect(value :int) -> bool:
    """Check if value is perfect"""
    end = value // 2
    total = 0
    if value < 6:
        return False
    for test in range(1, end + 1):
        if value % test == 0:
            total += test
    if total == value:
        return True
    return False

def properties(value :int) -> List:
    """Check parity of number and If number is armstrong"""
    my_list = []
    my_list.append("odd" if value % 2 == 1 else "even")
    if value < 1:
        return my_list
    total = 0
    temp = value
    count = 0
    while value > 0:
        count += 1
        value //= 10
    value = temp
    while value > 0:
        total += (value % 10) ** count
        value //= 10
    if total == temp:
        my_list.append("armstrong")
    return my_list


def digit_sum(value :int) -> int:
    """Returns the sum of the digits"""
    d_sum = 0
    while value > 0:
        d_sum += (value % 10)
        value //= 10
    return d_sum


def fun_fact(value :int) -> str:
    """Returns fun fact from an api call"""
    api = f"http://numbersapi.com/{value}"
    try:
        result = requests.get(api)
    except Exception as e:
        return "ConnectionError or HTTPError"
    return result.text



if __name__ == '__main__':
    app.run(port=5000)
