import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ShizukaXMusic import app
from ShizukaXMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^تفعيل$") & filters.group)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c6c72a67afca445b3175a.jpg",
caption=f"""**[᥉ᥱᥣᥣᥴƚ ᥣᥲ️ꪀᘜυᥲ️ᘜᥱ ƚ᥆ ᥣᥱᥲ️ᖇꪀ ꪔ᥆ᖇᥱ](https://t.me/N_G_12)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "عربي 🇪🇬", callback_data="arbic"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "English 🇺🇲", callback_data="english"),
                ],
            ]
        ),
    )


