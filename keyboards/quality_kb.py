from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def quality_keyboard():
    
    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton("480p", callback_data="480p"),
        InlineKeyboardButton("720p", callback_data="720p"),
        InlineKeyboardButton("1080p", callback_data="1080p")
    )

    return markup