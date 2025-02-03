# Number Classification API

This is a simple Python-based API that takes a number as an argument and returns facts about that number, including whether it is prime, perfect, Armstrong, or even/odd. If the number is invalid (non-numeric or any other issue), the API will return an error message in JSON format.

Built with Flask and Flask-CORS for cross-origin support.

## Task Description

Create an API that takes a number and returns interesting mathematical properties about it, along wi
th a fun fact.

## Features

Accepts a GET request with a number parameter.

Returns interesting mathematical properties about the number.

Includes a fun fact from the Numbers API about the number.

Handles CORS (Cross-Origin Resource Sharing).

Returns a 400 Bad Request if an invalid number is provided.


## API Endpoint

GET zealina-number-api.onrender.com/api/classify-number?number=\<number\>

### Example Request:

GET https://zealina-number-api.onrender.com/api/classify-number?number=371

Example Response (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

Example Response (400 Bad Request):
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation

1. Clone this repository to your local machine:
```sh
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Run the API locally:
```sh
python app.py
```

This will start the API on http://127.0.0.1:5000.



## Deployment

The API is deployed and publicly accessible. You can test the live version of the API at https://zealina-number-api.onrender.com/api/classify-number?number=\<number\>

## API Specifications
-   Query Parameter:
number: The number to classify (integer only).

-   Response Format:
200 OK: A valid response containing mathematical facts about the number.
400 Bad Request: When the provided number is not valid (e.g., non-numeric value).
