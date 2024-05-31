# utils/user_check.py
# User Check for InstaHacking.py
# Author: Sayed Sayedy

import requests

def user_exists(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 200
