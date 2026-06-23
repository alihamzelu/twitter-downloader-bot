from utils.state import user_state, user_data
from downloader.twitter_downloader import download_video
import os

def register_callback_handler(bot):

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):

        user_id = call.from_user.id
        quality = call.data

        if user_state.get(user_id) != "WAITING_QUALITY":
            return

        link = user_data[user_id]["link"]

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            f"⏳ Downloading {quality}..."
        )

        file_path = download_video(link, quality)

        bot.send_video(
            call.message.chat.id,
            video=open(file_path, "rb"),
            caption="✅ Done!"
        )

        os.remove(file_path)

        user_state.pop(user_id, None)
        user_data.pop(user_id, None)