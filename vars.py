#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22447622"))
API_HASH = environ.get("API_HASH", "543b62d58d3e723e766ba57a984ab65d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8448062014:AAEcVEUYxdcZlaGQUyIpkF7x9x8ww7C9--M")

OWNER = int(environ.get("OWNER", "777756062"))
CREDIT = environ.get("CREDIT", "KANHA 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6201066540').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6201066540').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
