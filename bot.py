from pyrogram import Client, filters
from pyrogram.types import Message
import os
from dotenv import load_dotenv
from affiliate_utils import convert_to_affiliate_link
from state_manager import load_config, update_config

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")
OWNER_ID = int(os.getenv("OWNER_ID"))

app = Client("userbot", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.private & filters.user(OWNER_ID))
async def handle_commands(client, message: Message):
    config = load_config()
    text = message.text.strip()
    args = text.split(maxsplit=1)
    command = args[0].lower()

    if command == "/start":
        await message.reply("✅ Userbot is alive.")
    elif command == "/status":
        await message.reply(str(config))
    elif command == "/add_source":
        config["source_channels"].append(args[1])
        update_config("source_channels", list(set(config["source_channels"])))
        await message.reply("✅ Source added.")
    elif command == "/remove_source":
        config["source_channels"].remove(args[1])
        update_config("source_channels", config["source_channels"])
        await message.reply("❌ Source removed.")
    elif command == "/add_dest":
        config["destination_channels"].append(args[1])
        update_config("destination_channels", list(set(config["destination_channels"])))
        await message.reply("✅ Destination added.")
    elif command == "/remove_dest":
        config["destination_channels"].remove(args[1])
        update_config("destination_channels", config["destination_channels"])
        await message.reply("❌ Destination removed.")
    elif command == "/add_prefix":
        update_config("prefix", args[1])
        await message.reply("✅ Prefix set.")
    elif command == "/remove_prefix":
        update_config("prefix", "")
        await message.reply("✅ Prefix removed.")
    elif command == "/add_suffix":
        update_config("suffix", args[1])
        await message.reply("✅ Suffix set.")
    elif command == "/remove_suffix":
        update_config("suffix", "")
        await message.reply("✅ Suffix removed.")
    elif command == "/clean_links":
        new_val = not config.get("clean_links", False)
        update_config("clean_links", new_val)
        await message.reply(f"✅ Clean links set to: {new_val}")
    elif command == "/reset_config":
        from state_manager import save_config, default_config
        save_config(default_config)
        await message.reply("♻ All settings reset.")

@app.on_message(filters.channel)
async def forward_handler(client, message: Message):
    config = load_config()
    src = str(message.chat.username or message.chat.id)
    if src not in config["source_channels"]:
        return

    text = message.text or message.caption or ""
    words = text.split()
    modified_words = [convert_to_affiliate_link(w) for w in words]

    if config.get("clean_links", False):
        modified_words = [w for w in modified_words if "amazon.in" in w or "flipkart.com" in w]

    final_text = f"{config['prefix']} {' '.join(modified_words)} {config['suffix']}".strip()

    for dest in config["destination_channels"]:
        try:
            await client.send_message(dest, final_text)
        except Exception as e:
            print(f"❌ Failed to forward to {dest}: {e}")

if __name__ == "__main__":
    print("🚀 Bot is running...")
    app.run()
