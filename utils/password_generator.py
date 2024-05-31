# utils/password_generator.py
# Password Generator for InstaHacking.py
# Author: Sayed Sayedy

import itertools

def get_personal_info():
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
    personal_info['company'] = input('Company: ')
    personal_info['special_characters'] = input('Special Characters (e.g., !@#$): ')
    return personal_info

def generate_passwords(filename, personal_info):
    base_passwords = [
        personal_info['first_name'], personal_info['last_name'], personal_info['nickname'],
        personal_info['pet_name'], personal_info['country'], personal_info['city'],
        personal_info['hobby'], personal_info['birthdate'], personal_info['favorite_movie'],
        personal_info['favorite_band'], personal_info['children_names'], personal_info['father_name'],
        personal_info['mother_name'], personal_info['partner_name'], personal_info['company']
    ]
    special_characters = personal_info['special_characters']
    permutations = set(base_passwords)

    for combo in itertools.permutations(base_passwords, 2):
        permutations.add(''.join(combo))
        permutations.add(''.join(combo) + special_characters)

    with open(filename, 'w') as f:
        for password in permutations:
            f.write(password + '\n')

def save_passwords(passwords, filename):
    with open(filename, 'a') as f:
        for password in passwords:
            f.write(password + '\n')
