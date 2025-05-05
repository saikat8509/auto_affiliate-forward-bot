# 🛍️ Auto Affiliate Forward Bot (Userbot-Based)

This bot automatically converts **Amazon and Flipkart** product links from other Telegram channels to your own **affiliate links**, and then **forwards them** to your destination channel(s).

It uses a **userbot** (based on `pyrogram`) so it can **monitor channels without admin access**.

---

## 🚀 Features

- ✅ Works without source channel admin access (userbot)
- ✅ Convert Amazon & Flipkart product links to your affiliate tags
- ✅ Supports multiple source and destination channels
- ✅ Add/remove channels via Telegram commands
- ✅ Add prefixes/suffixes to forwarded posts
- ✅ Automatically clean and keep only affiliate links
- ✅ Deployable to Koyeb

---

## 🧩 Requirements

- Python 3.8+
- Telegram API credentials: `API_ID`, `API_HASH`
- A Telegram **user session string** (not a bot token)

---

## 🔐 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saikat8509/auto_affiliate-forward-bot.git
cd auto_affiliate-forward-bot


🛠 Available Commands (Only Owner Can Use)
Send these commands to the userbot via private message:
| Command                           | Description                       |
| --------------------------------- | --------------------------------- |
| `/start`                          | Check if bot is alive             |
| `/status`                         | Show current config               |
| `/add_source @channelusername`    | Add a source channel              |
| `/remove_source @channelusername` | Remove a source channel           |
| `/add_dest @channelusername`      | Add a destination channel         |
| `/remove_dest @channelusername`   | Remove a destination channel      |
| `/add_prefix Your text`           | Add text before forwarded post    |
| `/remove_prefix`                  | Remove prefix                     |
| `/add_suffix Your text`           | Add text after forwarded post     |
| `/remove_suffix`                  | Remove suffix                     |
| `/clean_links`                    | Toggle clean-only-affiliate-links |
| `/reset_config`                   | Reset to default config           |

📦 Deployment on Koyeb
Push your repo to GitHub.

Create a new Koyeb service.

Choose GitHub > your repo.

Add .env variables via the Koyeb dashboard.

Set build command to:
pip install -r requirements.txt
Set run command to:
python bot.py

🧠 Notes
This bot uses a user account (not a bot token).

You must generate a SESSION_STRING using Pyrogram.

Avoid spamming too many channels at once to prevent Telegram limits.

