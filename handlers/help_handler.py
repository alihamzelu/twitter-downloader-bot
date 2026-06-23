def register_help_handler(bot):

    @bot.message_handler(commands=['help'])
    def help(message):

        HELP_TEXT = """📥 Twitter (X) Video Downloader

✨ How to use:
1️⃣ Send a Twitter/X video link
2️⃣ Choose video quality
3️⃣ Get your video instantly

⚡ Supported:
• x.com
• twitter.com

💡 Just send a link and I’ll do the rest.
"""

        bot.send_message(
            message.chat.id,
            HELP_TEXT
        )