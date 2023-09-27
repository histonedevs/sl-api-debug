import requests
import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def get_headers():
    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.environ['SL_ACCESS_TOKEN']}"
    }


def get_refresh_tokens():
    #reload changes if there is an update from some other process
    dotenv.load_dotenv(dotenv_file)

    response = requests.post(
        f"{os.environ['SL_API_ENDPOINT']}/oauth/token",
        json={
            "grant_type": "refresh_token",
            "client_id": os.environ['SL_CLIENT_ID'],
            "client_secret": os.environ['SL_CLIENT_SECRET'],
            "refresh_token": os.environ['SL_REFRESH_TOKEN'],
        }
    )

    if response.status_code == 200:
        print("Success!")
        tokens = response.json()
        # Write changes to .env file.
        dotenv.set_key(dotenv_file,'SL_ACCESS_TOKEN', tokens["access_token"])
        dotenv.set_key(dotenv_file,'SL_REFRESH_TOKEN', tokens["refresh_token"])
        # Reload Environment
        dotenv.load_dotenv(dotenv_file)
    else:
        print(f"There's a {response.status_code} error with your request")


def get_sales_data(parameters):
    dotenv.load_dotenv(dotenv_file)

    response = requests.get(
        f"{os.environ['SL_API_ENDPOINT']}/api/sales/per-day-per-product",
        params=parameters,
        headers=get_headers()
    )

    if response.status_code == 200:
        print("Successfully fetched sales-per-day!")
        # print(response.json())
    else:
        print(f"There's a {response.status_code} error with your request")

    return response.status_code


def get_cogs_data(parameters):
    dotenv.load_dotenv(dotenv_file)

    response = requests.get(
        f"{os.environ['SL_API_ENDPOINT']}/api/cogs/cost-periods",
        params=parameters,
        headers=get_headers()
    )

    if response.status_code == 200:
        print("Successfully fetched cogs!")
        # print(response.json())
    else:
        print(f"There's a {response.status_code} error with your request")

    return response.status_code
