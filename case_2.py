import time

import client


def call_cogs_endpoint():
    status_code = client.get_cogs_data({
        "seller_id": "A1LVK69OFB830W",
        "marketplace_id": "ATVPDKIKX0DER",
        "sku": "EK-N2O-48"
    })

    print(f"status_code: {status_code}")


def run_case_2(attempt):
    print(f"attempt#{attempt}")
    # Case 2: A more realistic scenario where we call the Sales per day per product Endpoint, Or the COGS update endpoint.
    # 1. Get new refresh and access tokens from the Auth API  ===> [They are present in .env]
    # 2. Call the Sales per day per product API, or COGS API, they behave as expected
    call_cogs_endpoint()

    # 3. Try to refresh the tokens via the auth endpoint
    # 4. We get the message that the tokens are revoked.
    if client.refresh_tokens():
        print("Token Refresh Successful")
    else:
        print("Tokens could not be refreshed")

    # 5. We cannot call the Auth API nor any other endpoint because tokens have expired and we have not got new ones.
    call_cogs_endpoint()


attempt = 0
while True:
    attempt = attempt + 1

    run_case_2(attempt)

    print("Will try again after 5 secs")
    time.sleep(5)
