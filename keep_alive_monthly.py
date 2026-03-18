import requests
import logging
import configparser

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
USERNAME = config['DEFAULT']['username']
PASSWORD = config['DEFAULT']['password']

def auto_login():
    try:
        logging.info('Starting the auto-login process...')
        login_url = 'https://example.com/login'  # Replace with actual login URL
        payload = {'username': USERNAME, 'password': PASSWORD}

        # Send login request
        response = requests.post(login_url, data=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if 'success' in response.text:
            logging.info('Login successful!')
            # Proceed with the rest of the script
        else:
            logging.error('Login failed: Credentials are incorrect.')

    except requests.exceptions.RequestException as e:
        logging.error(f'An error occurred while trying to login: {e}')  

if __name__ == '__main__':
    auto_login()