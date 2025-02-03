# Number Classification API

## Task Description
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## API Specification
 Endpoint: GET** <your-domain.com>/api/classify-number?number=371
 ```json
 Required JSON Response Format (200 OK):
 {
     "number": 371,
     "is_prime": false,
     "is_perfect": false,
     "properties": ["armstrong", "odd"],
     "digit_sum": 11,  // sum of its digits
     "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
 }
 ```
 Required JSON Response Format (400 Bad Request)
 ```json
 {
     "number": "alphabet",
     "error": true
 }
 ```
