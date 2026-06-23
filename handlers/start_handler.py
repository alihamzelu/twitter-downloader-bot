from keyboards.main_kb import main_keyboard

def register_start_handler(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        bot.send_message(
            message.chat.id,
            f"""👋 Welcome, {message.from_user.first_name}!

📥 Twitter (X) Video Downloader Bot

✨ Send me a video link and I’ll download it for you instantly.

🚀 Fast • Simple • Free
""",
            reply_markup=main_keyboard()
        )