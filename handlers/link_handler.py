import re
from keyboards.quality_kb import quality_keyboard
from utils.state import user_data, user_state

twitter_pattern = r"(https?://(www\.)?(x\.com|twitter\.com)/\S+)"

def register_link_handler(bot):

    @bot.message_handler(func=lambda m: True)
    def handle_link(message):

        text = message.text or ""
        user_id = message.from_user.id

        match = re.search(twitter_pattern, text)

        if match:
            link = match.group(1)

            user_state[user_id] = "WAITING_QUALITY"
            user_data[user_id] = {"link": link}

            bot.send_message(
                message.chat.id,
                "🎬 Great! Now choose video quality:",
                reply_markup=quality_keyboard()
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Please send a valid Twitter/X video link."
            )