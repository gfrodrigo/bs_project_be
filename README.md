# BS Backend Project
This is a backend of a test project

Please first install the requirements:

`pip install -r requirements.txt`

This project also has configured pytest, so you can run test with command:

`pytest`

The endpoint to validate the business credit is:

http://localhost:8000/api/validate_credit/

the expected json:

`{"tax_id":"10-0001", "name":"My Business Company", "annual_revenue": 500000}`

the response can be ("Declined", "Undecided", "Approved"):
example: 

`{"data":"Undecided"}`
