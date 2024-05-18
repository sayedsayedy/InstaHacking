# utils/password_generator.py
# Author: Sayed Sayedy
# Ethical Hacker & Digital Forensics Investigator

import random
import itertools

def get_personal_info():
    """
    Collects personal information from the user to generate passwords.

    Returns:
        dict: A dictionary containing the user's personal information.
    """
    personal_info = {}
    personal_info['first_name'] = input('First Name: ')
    personal_info['last_name'] = input('Last Name: ')
    personal_info['nickname'] = input('Nickname: ')
    personal_info['pet_name'] = input('Pet Name: ')
    personal_info['country'] = input('Country: ')
    personal_info['city'] = input('City: ')
    personal_info['hobby'] = input('Hobby: ')
    personal_info['birthdate'] = input('Birthdate (YYYYMMDD): ')
    personal_info['favorite_movie'] = input('Favorite Movie: ')
    personal_info['favorite_band'] = input('Favorite Band: ')
    personal_info['children_names'] = input('Children Names: ')
    personal_info['father_name'] = input('Father Name: ')
    personal_info['mother_name'] = input('Mother Name: ')
    personal_info['partner_name'] = input('Partner Name: ')
    personal_info['company'] = input('Company (Employer): ')
    personal_info['special_characters'] = input('Special Characters (optional): ')
    return personal_info

def generate_passwords(file_path, personal_info):
    """
    Generates a list of passwords based on the provided personal information and saves them to a file.

    Args:
        file_path (str): The file path to save the generated passwords.
        personal_info (dict): A dictionary containing the user's personal information.
    """
    combinations = [
        personal_info['first_name'],
        personal_info['last_name'],
        personal_info['nickname'],
        personal_info['pet_name'],
        personal_info['country'],
        personal_info['city'],
        personal_info['hobby'],
        personal_info['birthdate'],
        personal_info['favorite_movie'],
        personal_info['favorite_band'],
        personal_info['children_names'],
        personal_info['father_name'],
        personal_info['mother_name'],
        personal_info['partner_name'],
        personal_info['company']
    ]

    years = ['2022', '2023', '2024']
    special_characters = personal_info['special_characters'] if personal_info['special_characters'] else '!@#$%^&*'

    passwords = set()
    for combo in itertools.product(combinations, repeat=2):
        for year in years:
            for special_char in special_characters:
                passwords.add(f'{combo[0]}{combo[1]}{year}{special_char}')
                passwords.add(f'{combo[0]}{year}{combo[1]}{special_char}')
                passwords.add(f'{year}{combo[0]}{combo[1]}{special_char}')
                passwords.add(f'{combo[0]}{combo[1]}{special_char}{year}')

    with open(file_path, 'r+') as file:
        existing_passwords = file.read().splitlines()
        passwords = list(passwords) + existing_passwords
        file.seek(0)
        file.write('\n'.join(passwords))
        file.truncate()

    print(f'Passwords generated and saved to {file_path}')

def save_passwords(passwords, file_path):
    """
    Saves the given passwords to a file.

    Args:
        passwords (list): A list of passwords to be saved.
        file_path (str): The file path to save the passwords.
    """
    with open(file_path, 'a') as file:
        for password in passwords:
            file.write(f'{password}\n')
