# main.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, SESSION_STRING, SOURCE_CHANNELS, DESTINATION_CHANNELS, DEFAULT_CAPTION
from affiliate_utils import convert_to_cuelinks
import re

# Initialize userbot session using session string
app = Client(
    session_name=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

# Pattern to find product links
PRODUCT_LINK_PATTERN = r"(https?://[^\s]+)"

@app.on_message(filters.channel & filters.chat(SOURCE_CHANNELS))
async def forward_affiliate_post(client: Client, message: Message):
    if not message.text and not message.caption:
        return

    text = message.text or message.caption or ""
    urls = re.findall(PRODUCT_LINK_PATTERN, text)

    if not urls:
        return

    updated_text = text
    for url in urls:
        if "myntra.com" in url or "meesho.com" in url:
            affiliate_url = convert_to_cuelinks(url)
            updated_text = updated_text.replace(url, affiliate_url)

    # Forward the message to all destination channels
    for dest in DESTINATION_CHANNELS:
        try:
            if message.photo:
                await client.send_photo(dest, photo=message.photo.file_id, caption=updated_text)
            elif message.video:
                await client.send_video(dest, video=message.video.file_id, caption=updated_text)
            else:
                await client.send_message(dest, updated_text)
        except Exception as e:
            print(f"Error forwarding to {dest}: {e}")

print("Userbot is running with session...")
app.run()
