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


@app.route('/api/classify-number')
def classify_number():
    """Return the properties and fun facts of the number"""
    if len(request.args) > 1 or request.args.get('number') is None:
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


def is_prime(value: int) -> bool:
    """
    Description: Check if value is a prime

    A prime number is a natural number greater than 1 that is only
    divisible by 1 and itself
    e.g 2, 3, 5, 7, 11, 13 e.t.c

    for more information visit https://en.wikipedia.org/wiki/Prime_number
    """
    if (value <= 3):
        return value > 1
    if value % 6 not in [1, 5]:
        return False
    for p, q in ((i, i + 2) for i in range(5, int(value ** 0.5) + 1, 6)):
        if (value % p == 0 or value % q == 0):
            return False
    return True


def is_perfect(value: int) -> bool:
    """
    Description: Check if value is perfect

    A perfect number is a number that the sum of all positive integer factors
    excluding itself add up to the number
    e.g 6
        Factors of 6: 1, 2, 3, (6)
        Calculation; 1 + 2 + 3 = 6 (Excluding 6 as a factor)
    Hence, 6 is a perfect number
    for more information visit https://en.wikipedia.org/wiki/Perfect_number
    """
    end = value // 2
    total = 1
    if value < 6:
        return False
    for test in range(2, end + 1):
        if value % test == 0:
            total += test
    if total == value:
        return True
    return False


def properties(value: int) -> List:
    """
    Description: Check parity of number and if number is armstrong.

    - Parity of a number is its attribute of being an even or odd number
    for more info visit https://en.wikipedia.org/wiki/Parity_(mathematics)

    - An armstrong number is a natural number such that the sum of each of its
    digits raised to the power of number of digits in the number is equal to
    the number itself e.g 153
        Number of digits: 153 has 3 digits.
        Calculation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    for further reading visit https://en.wikipedia.org/wiki/Narcissistic_number

    Return: A list with the parity, armstrong if number is armstrong
    """
    my_list = ["odd" if value % 2 == 1 else "even"]
    if value < 1:
        return my_list
    total = 0
    temp = value
    count = 0
    while temp > 0:  # Number of digits in value
        count += 1
        temp //= 10
    temp = value
    while temp > 0:  # Raise to power of count and add to running total
        total += (temp % 10) ** count
        temp //= 10
    if total == value:
        my_list.append("armstrong")
    return my_list


def digit_sum(value: int) -> int:
    """Returns the sum of the digits of value"""
    d_sum = 0
    while value > 0:
        d_sum += (value % 10)
        value //= 10
    return d_sum


def fun_fact(value: int) -> str:
    """Returns fun fact from an api call"""
    api = f"http://numbersapi.com/{value}"
    try:
        result = requests.get(api)
    except Exception as e:
        return f"Error: {e}"
    return result.text


if __name__ == '__main__':
    app.run(port=5000)
