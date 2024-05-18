import requests

def user_exists(user):
    url = f'https://www.instagram.com/{user}/'
    response = requests.head(url)
    return response.status_code == 200
