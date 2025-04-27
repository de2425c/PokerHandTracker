import requests
import json
import os

# Get the mkcert root certificate path

# Make the request with proper certificate verification
response = requests.post(
    'http://localhost:8000/parse-hand',
    json={"description": "Blinds 1/3, I raised to $10 from the cutoff with pocket Jacks, big blind called, $600 effective. Flop came Queen-Nine-Three with two hearts, he checked, I bet $15, he called. Turn was a blank Five, we both checked. River was a Jack, he led for $40, I raised to $120, he folded."},
)

# Option 2: Use the mkcert root certificate
# Uncomment these lines if you want to use the root certificate instead
# response = requests.post(
#     'https://localhost:5000/parse-hand',
#     json={"description": "your hand history here"},
#     verify='/Users/davideyal/Library/Application Support/mkcert/rootCA.pem'  # Path to mkcert root certificate
# )

print(response.status_code)
print(json.dumps(response.json(), indent=2))