import client
import time


attempt = 0
while True:
    attempt += 1
    print(f"Attempt: {attempt}")

    status_code = client.get_cogs_data({
        "seller_id": "A1LVK69OFB830W",
        "marketplace_id": "ATVPDKIKX0DER",
        "sku": "EK-N2O-48"
    })

    print(f"status_code: {status_code}")

    time.sleep(5)

    if status_code == 401:
        print("++++++ Get Token Refresh On Expiry ++++++")
        client.refresh_tokens()

