from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import get_assistant




@app.on_message(filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3e46bfad79e017c69ff69.jpg",
caption=f"""**- اهلين ياحلو  {message.from_user.mention}\n\n شكرآ لاستضافتي الي مجموعتك لمعرفة كيفة استخدامي وطريقة التشغيل اضغط على زر بأسغل 👇**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                
                    InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data="arbic"),
                ],
            ]
        ),
    )


