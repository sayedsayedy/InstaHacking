# Instagram Security Testing Tool

## Overview
A powerful tool designed by Sayed Sayedy for ethical hacking and security testing on Instagram. It identifies weak passwords and security vulnerabilities in Instagram accounts.

## Features
- Username existence check
- Password brute-force attack
- Custom and generated password lists
- Multi-threaded operations
- Login result categorization (success, 2FA required, checkpoint, failure)

**Disclaimer:** This tool is intended for use by authorized personnel only. Misuse of this tool for unauthorized access to accounts is illegal and unethical.

## Usage

### Prerequisites

- Ensure you have proper authorization to test the account.
- Python 3.x
- Requests library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ssayedy/InstagramSecurityTestingTool
    cd InstagramSecurityTestingTool
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Tool

1. Run the main script:
    ```bash
    python InstagramSecurityTestingTool.py
    ```

2. Enter the username and path to the password list when prompted.

3. The script will attempt to log in using the provided credentials and output the results.

### Output

- Successful logins are saved in `success.txt`.
- Accounts requiring two-factor authentication are saved in `two_factor.txt`.
- Accounts requiring additional verification are saved in `checkpoint.txt`.

### Example

Here is an example of how to run the tool:

```bash
$ python InstagramSecurityTestingTool.py
Username: example_user
Password List: passwords.txt
  ```
### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ssayedy/InstagramSecurityTestingTool/blob/main/LICENSE.rst) file for details.

### Author

Sayed Sayedy - Ethical Hacker & Digital Forensics Investigator