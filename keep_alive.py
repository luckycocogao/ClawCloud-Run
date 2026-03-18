import time
import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler

# Load configuration from a JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Function to send Telegram notifications
def send_telegram_notification(message):
    bot_token = config['telegram_bot_token']
    chat_id = config['telegram_chat_id']
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=payload)

# Function to keep the bot alive
def keep_alive():
    # Your keep-alive code here, replace the URL with your actual endpoint
    url = config['keep_alive_url']
    response = requests.get(url)
    if response.status_code == 200:
        send_telegram_notification('Keep-alive successful')
    else:
        send_telegram_notification('Keep-alive failed')

# Schedule the keep_alive function to run monthly
scheduler = BlockingScheduler()
scheduler.add_job(keep_alive, 'interval', months=1)

if __name__ == '__main__':
    print('Starting the keep-alive bot...')
    scheduler.start()