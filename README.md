# Instagram Password Cracker

## Super Ethical Hacking Tool for Pentesting by Sayed Sayedy

## Description
This tool is designed for ethical hackers to identify security vulnerabilities and weak passwords in Instagram accounts. Ensure you have proper authorization before using this tool.

## Features
- Brute-force attack using custom and generated password lists.
- Generates passwords based on user-provided personal information.
- Multi-threaded to enhance the speed of the attack.
- Session saving for resuming an interrupted attack.
- Utilizes Tor for anonymous and secure connections.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sayedsayedy/InstaHacking
    cd InstaHacking
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the Tor service:
    ```bash
    sudo service tor start
    ```

2. Run the script:
    ```bash
    python InstaHacking.py
    ```

3. Follow the prompts to enter the username and choose the password generation method.

## Requirements
Ensure you have the following installed on your system:

- Tor:
    ```bash
    sudo apt-get install tor
    ```
- Python 3.x
- `requests` library
- `six` library

## License
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is provided for educational and ethical purposes only. Misuse of this script for unauthorized access to Instagram accounts is illegal and unethical. By using this script, you agree that Sayed Sayedy is not responsible for any illegal or unauthorized use. Use this tool responsibly and only on accounts for which you have explicit permission.
