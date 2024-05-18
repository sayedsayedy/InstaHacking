# utils/user_check.py
# Author: Sayed Sayedy
# Ethical Hacker & Digital Forensics Investigator

import requests
import re
import time
import logging
from fake_useragent import UserAgent

# Setup logging
logging.basicConfig(filename='user_check_log.txt', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

ua = UserAgent()

def get_headers():
    """
    Generates dynamic headers for the HTTP request.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    return headers

def user_exists(username, retries=3, delay=2):
    """
    Checks if a user exists on Instagram.

    Args:
        username (str): The Instagram username to check.
        retries (int): The number of retries in case of a network failure.
        delay (int): The delay in seconds between retries.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    url = f'https://www.instagram.com/{username}/'
    for attempt in range(retries):
        try:
            headers = get_headers()
            response = requests.get(url, headers=headers, timeout=10)
            logging.info(f'Attempt {attempt + 1}: Checked user {username} with headers {headers}')
            if response.status_code == 200 and 'Page Not Found' not in response.text:
                logging.info(f'User {username} exists.')
                return True
            else:
                logging.warning(f'User {username} does not exist or page not found.')
                return False
        except requests.RequestException as e:
            logging.error(f'Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...')
            print(f'Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...')
            time.sleep(delay)
    logging.error(f'User {username} could not be verified after {retries} attempts.')
    return False

def get_user_info(username):
    """
    Fetches user information from Instagram.

    Args:
        username (str): The Instagram username to fetch information for.

    Returns:
        dict: A dictionary containing user information if available, None otherwise.
    """
    url = f'https://www.instagram.com/{username}/?__a=1'
    try:
        headers = get_headers()
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            user_info = response.json()
            logging.info(f'Fetched information for user {username} with headers {headers}')
            return user_info
        else:
            logging.warning(f'Failed to fetch information for user {username}')
            return None
    except requests.RequestException as e:
        logging.error(f'Failed to fetch information for user {username}: {e}')
        return None

def check_username_format(username):
    """
    Checks if the provided username format is valid.

    Args:
        username (str): The Instagram username to check.

    Returns:
        bool: True if the username format is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.]+$'
    if re.match(pattern, username):
        logging.info(f'Username {username} has a valid format.')
        return True
    else:
        logging.warning(f'Username {username} has an invalid format.')
        return False
