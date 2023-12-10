import os
import telebot
from opyngpt import prompt
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("Telegram bot token (TOKEN) not set in environment variables.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message)
    result = prompt(message.text)
    bot.reply_to(message, result, parse_mode='Markdown')

bot.infinity_polling()
