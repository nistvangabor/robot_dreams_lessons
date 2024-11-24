import requests

def send_telegram_message(bot_token: str, chat_id: int, message: str):
    """
    Sends a message to a Telegram chat using the Bot API.
    
    :param bot_token: The API token for your bot.
    :param chat_id: The chat ID of the recipient.
    :param message: The message text to send.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status: {response.status_code}, Error: {response.text}")

# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# ping <ip>