import os

api_id = 20567114
api_hash = os.environ.get("API_HASH", "8a5b92106e45fc6637a65a67df060a65")
bot_token = os.environ.get("7863736606:AAFNyv9PxoAh46PrIAcAl-SbbcvpLcfxNdU")
auth_users = os.environ.get("AUTH_USERS", "8036182138")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "8036182138")
owner_users = [int(num) for num in osowner_users.split(",")]
