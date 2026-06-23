import telebot
from config import API_TOKEN
from handlers import register_all_handlers
from handlers.callback_handler import register_callback_handler


bot = telebot.TeleBot(API_TOKEN)

register_all_handlers(bot)
register_callback_handler(bot)


bot.polling()