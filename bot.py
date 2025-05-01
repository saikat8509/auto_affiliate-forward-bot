from pyrogram import Client, filters
from config import *
from affiliate_utils import clean_text, convert_to_affiliate
import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

app = Client("userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.chat(SOURCE_CHANNELS))
def forward_message(client, message):
    try:
        source = message.chat.username or message.chat.id
        logging.info(f"Received message from: {source}")

        content = message.text or message.caption or ""
        content = clean_text(content)
        content = convert_to_affiliate(content)
        content = f"{content}\n\n{CUSTOM_CAPTION}"

        for dest in DEST_CHANNELS:
            if message.photo:
                client.send_photo(dest, message.photo.file_id, caption=content)
            elif message.video:
                client.send_video(dest, message.video.file_id, caption=content)
            elif message.document:
                client.send_document(dest, message.document.file_id, caption=content)
            elif message.text:
                client.send_message(dest, content)
            logging.info(f"Forwarded message to: {dest}")

    except Exception as e:
        logging.error(f"Error: {e}")

app.run()
