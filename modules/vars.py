import os

API_ID    = os.environ.get("API_ID", "23049236")
API_HASH  = os.environ.get("API_HASH", "ec484a6d8975243b01e7b91c6585469e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7919888960:AAEzGDJRn3k--czfvIE6W2Yv6azT37bce-4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
