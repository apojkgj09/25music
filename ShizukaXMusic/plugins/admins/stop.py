from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ShizukaXMusic import app

from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import set_loop
from ShizukaXMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
STOP_COMMAND_chh = get_command("STOP_COMMAND_chh")


@app.on_message(
    filters.command(STOP_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@app.on_message(
    filters.command(["انهاء","ايقاف","لندا طفيها"],"") & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Shizuka.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention), disable_web_page_preview=True
    )

@app.on_message(
    filters.command(STOP_COMMAND_chh) & filters.channel & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music_ch(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Shizuka.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    if message.sender_chat:
        mention = f'<a href=tg://user?id={message.chat.id}>{message.chat.title}</a>'
    else:
        mention = message.from_user.mention
    await message.reply_text(
        _["admin_9"].format(mention)
    )
