# Instagram Security Testing Tool

## Author
Sayed Sayedy

## Description
This tool is designed for ethical hackers to identify security vulnerabilities and weak passwords in Instagram accounts. Ensure you have proper authorization before using this tool.

## Features
- Brute-force attack using custom and generated password lists.
- Generates passwords based on user-provided personal information.
- Multi-threaded to enhance the speed of the attack.
- Does not generate `.pyc` files.
- No log files are created; all activities are output to the console.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ssayedy/InstagramSecurityTestingTool
    cd InstagramSecurityTestingTool
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the tool:
    ```bash
    python InstagramSecurityTestingTool.py
    ```

2. Follow the prompts to enter the username and choose the password generation method.

## Requirements
- Python 3.x
- `requests` library
- `six` library

## License
This project is licensed under the MIT License - see the [LICENSE.rst](LICENSE.rst) file for details.

## Disclaimer
This tool is intended for ethical use only. Ensure you have proper authorization before using it on any Instagram account.
