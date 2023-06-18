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
        photo=f"https://telegra.ph/file/3e46bfad79e017c69ff69.jpg",
caption=f"""**-› جميع اوامر البوت موجودة بالاسفل**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "عربي 🇪🇬", callback_data="arbic"
                ),
                
                    InlineKeyboardButton(
                        "English 🇺🇲", callback_data="english"),
                ],
            ]
        ),
    )


