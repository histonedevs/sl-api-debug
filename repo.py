import dotenv

dotenv_file = dotenv.find_dotenv()

def reload_keys_from_repo():
    dotenv.load_dotenv(dotenv_file, override=True)

def save_keys_in_repo(tokens):
    dotenv.set_key(dotenv_file, 'SL_ACCESS_TOKEN', tokens["access_token"])
    dotenv.set_key(dotenv_file, 'SL_REFRESH_TOKEN', tokens["refresh_token"])

reload_keys_from_repo()