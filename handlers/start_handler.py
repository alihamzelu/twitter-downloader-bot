from keyboards.main_kb import main_keyboard

def register_start_handler(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        bot.send_message(
            message.chat.id,
            f"Welcome To Twitter Video Downloader {message.from_user.first_name} \n Send me a Twitter/X post link and I'll download the video for you.",
            reply_markup=main_keyboard()
        )