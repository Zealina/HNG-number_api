#!/usr/bin/env python3
"""Test my API from 0 to 100"""


import requests
import json

result = []
for i in range(99, 301, 2):
    link = f'http://localhost:5000/api/classify-number?number={i}'
    result.append(requests.get(link).json())

with open('sample_test', 'w') as fp:
    json.dump(result, fp, indent=4)

