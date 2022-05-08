import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bookogram import bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if __name__ == "__main__":
    bot.start(bot_token=BOT_TOKEN)
