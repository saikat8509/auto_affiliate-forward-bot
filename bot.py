from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_STRING, SOURCE_CHANNELS, DEST_CHANNELS, REMOVE_KEYWORDS, CUSTOM_CAPTION
from affiliate_utils import extract_links, convert_affiliate_link

app = Client("affiliate_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

def clean_text(text):
    for word in REMOVE_KEYWORDS:
        text = text.replace(word, "")
    return text.strip()

@app.on_message(filters.chat(SOURCE_CHANNELS) & (filters.text | filters.caption))
def forward_with_affiliate(client, message):
    original_text = message.caption if message.caption else message.text
    if not original_text:
        return

    links = extract_links(original_text)
    modified_text = original_text

    for link in links:
        affiliate_link = convert_affiliate_link(link)
        modified_text = modified_text.replace(link, affiliate_link)

    modified_text = clean_text(modified_text)
    final_text = f"{modified_text}\n\n{CUSTOM_CAPTION}"

    for dest in DEST_CHANNELS:
        try:
            if message.photo:
                client.send_photo(dest, photo=message.photo.file_id, caption=final_text)
            elif message.video:
                client.send_video(dest, video=message.video.file_id, caption=final_text)
            else:
                client.send_message(dest, final_text)
        except Exception as e:
            print(f"Failed to forward to {dest}: {e}")

app.run()
