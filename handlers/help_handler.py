

def register_help_handler(bot):

    @bot.message_handler(commands=['help'])
    def help(message):
        HELP_TEXT = """📥 Twitter (X) Video Downloader

        How to use:
        1️⃣ Send a tweet link
        2️⃣ Download your video


        ✅ Supported:
        • x.com

        💡 Just send the link and the bot will do the rest.
        """
        bot.send_message(
            message.chat.id,
            HELP_TEXT
        )