""" 
Python Script to get a token needed to login into Rubrik Security Cloud
Define: 
    rsc_url - RSC_URL Customer name so it matches your company RSC URL
"""

import requests
import sys

# RSC Customer URL, change this to your URL provided by Rubrik
rsc_url = "https://[CUSTOMER-NAME].my.rubrik.com]"

# Generate API token with RSC service account client id and secret
token_url = rsc_url + "/api/client_token"
token_headers = {
    "Content-Type": "application/json"
}
token_data = {
    "client_id": f"[YOUR SERVICE USER CLIENT ID]",
    "client_secret": f"[YOUR SERVICE USER CLIENT SECRET]"
}

try:
    token_response = requests.post(token_url, headers=token_headers, json=token_data)
    if token_response.status_code == 200:
        api_token = token_response.json().get('access_token')
        print("\nToken: \n" + api_token + "\n")
    else: 
        print(f"Request failed with status code {token_response.status_code}") 
except Exception as err:
    print(f"An error ocurred: {err}")
    sys.exit(1)