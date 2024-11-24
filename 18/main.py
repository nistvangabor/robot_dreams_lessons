
import os
from email_sender import EmailSender
from telegram import send_telegram_message
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    email_sender = EmailSender(sender="nigrushid@gmail.com", passcode=os.environ.get("GMAIL_PW"))
    
    email_sender.send_email(
        to=["nigrushid@gmail.com"],
        subject="Test Email!",
        body={
            "html_template_path": "18/email_template.html",  # Path to your HTML template
            "params": {  # Variables to replace in the template
                "user_name": "Test Simon",
                "year": "2024"
            },
            "text": "This is a plain text fallback for clients that do not support HTML."
        },
        attachments=None  # Attachments can be added here
    )

    BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID") 
    MESSAGE = f"Hello, this is a message from the VPS!"
    
    send_telegram_message(BOT_TOKEN, CHAT_ID, MESSAGE)
