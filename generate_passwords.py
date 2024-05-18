import itertools
import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_passwords(file_path, count=100):
    with open(file_path, 'w') as f:
        for _ in range(count):
            f.write(generate_strong_password() + '\n')

base_words = ["Muenchen", "Munich"]
years = ["2024"]
special_chars = [".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
substitutions = {"a": "4", "e": "3", "i": "1", "o": "0"}

def generate_variations(word):
    variations = set()
    for char, sub in substitutions.items():
        if char in word:
            variations.add(word.replace(char, sub))
    return variations

passwords = set()

for base_word in base_words:
    for year in years:
        # Base passwords
        passwords.add(f"{base_word}{year}")
        passwords.add(f"{base_word}.{year}")
        passwords.add(f"{base_word}{year}!")
        passwords.add(f"{base_word}.{year}!")
        
        # Variations with substitutions
        variations = generate_variations(base_word)
        for variation in variations:
            passwords.add(f"{variation}{year}")
            passwords.add(f"{variation}.{year}")
            passwords.add(f"{variation}{year}!")
            passwords.add(f"{variation}.{year}!")
        
        # Passwords with special characters
        for special_char in special_chars:
            passwords.add(f"{base_word}{year}{special_char}")
            passwords.add(f"{base_word}.{year}{special_char}")
            passwords.add(f"{base_word}{special_char}{year}")
            passwords.add(f"{base_word}{year}{special_char}!")
            passwords.add(f"{base_word}.{year}{special_char}!")
            passwords.add(f"{base_word}{special_char}.{year}!")
            passwords.add(f"{base_word}{special_char}{year}!")
            
            for variation in variations:
                passwords.add(f"{variation}{year}{special_char}")
                passwords.add(f"{variation}.{year}{special_char}")
                passwords.add(f"{variation}{special_char}{year}")
                passwords.add(f"{variation}{year}{special_char}!")
                passwords.add(f"{variation}.{year}{special_char}!")
                passwords.add(f"{variation}{special_char}.{year}!")
                passwords.add(f"{variation}{special_char}{year}!")
                
# Write to passwords.txt
with open("passwords.txt", "w") as f:
    for password in passwords:
        f.write(password + "\n")

print("Generated passwords saved to passwords.txt")
