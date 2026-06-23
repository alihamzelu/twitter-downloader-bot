from utils.state import user_state, user_data
from downloader.twitter_downloader import download_video
import os

def register_callback_handler(bot):

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        user_id = call.from_user.id
        quality = call.data

        # ❌ بررسی استیت
        if user_state.get(user_id) != "WAITING_QUALITY":
            bot.answer_callback_query(call.id, "Session expired", show_alert=True)
            return

        # 🛡️ دریافت ایمن لینک
        data = user_data.get(user_id)
        if not data or "link" not in data:
            bot.answer_callback_query(call.id, "Data not found. Try again.")
            user_state.pop(user_id, None)
            return

        link = data["link"]
        bot.answer_callback_query(call.id)

        # 🧼 ویرایش پیام قبلی و حذف کیبورد (جلوگیری از ارسال پیام تکراری)
        bot.edit_message_text(
            text=f"⏳ Downloading {quality}p...",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )

        file_path = None

        try:
            # 📥 دانلود ویدیو
            file_path = download_video(link, quality)

            if file_path and os.path.exists(file_path):
                # 📤 ارسال ویدیو با مدیریت صحیح فایل (with open)
                with open(file_path, "rb") as video_file:
                    bot.send_video(
                        call.message.chat.id,
                        video=video_file,
                        caption=f"✅ Done! ({quality}p)"
                    )
                
                # 🧹 حذف پیام "در حال دانلود" بعد از موفقیت
                bot.delete_message(call.message.chat.id, call.message.message_id)
            else:
                raise Exception("File not found after download")

        except Exception as e:
            print(f"Error: {e}") # برای لاگ خودتان
            bot.send_message(
                call.message.chat.id,
                "❌ Download failed. Please try another link."
            )

        finally:
            # 🧹 حذف فایل (حالا بدون مشکل قفل شدن فایل اجرا می‌شود)
            if file_path and os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete file: {e}")

            # 🧠 پاک کردن state و data
            user_state.pop(user_id, None)
            user_data.pop(user_id, None)