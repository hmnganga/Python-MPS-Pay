import requests
from access_token import generate_access_token
import keys
from requests.auth import HTTPBasicAuth




def register_url():
    my_access_token = generate_access_token()

    api_url ="https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
    
    "ShortCode": keys.shortcode,
    "ResponseType":"Completed",
    "ConfirmationURL":"https://sleepy-atoll-56664.herokuapp.com/api/payments/c2b-confirmation/",
    "ValidationURL":"https://sleepy-atoll-56664.herokuapp.com/api/payments/c2b-validation/",

    }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()

def simulate_c2b_transaction():
    my_access_token = generate_access_token()


    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
    "ShortCode": keys.shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"2",
    "Msisdn":keys.test_msisdn,
    "BillRefNumber":"34516723" }

    response = requests.post(api_url, json=request, headers=headers)

    print (response.text)
    
simulate_c2b_transaction()