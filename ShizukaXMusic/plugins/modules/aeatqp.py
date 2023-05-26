import asyncio
import os
from pyrogram.types import CallbackQuery
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["المطور","مطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d454e6154b8a33352710c.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : »» [𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 ¹](https://t.me/FHK_M5)
◉ 𝚄𝚂𝙴𝚁 : »» @FHK_M5
◉ 𝙸𝙳   : »» 6230638204
◉ 𝙱𝙸𝙾  : »» **- لم يعد بالي يُبالي فـ ليحترق ڪًٰل شي**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 ²", url=f"https://t.me/FHK_M5"),
                ],[
                InlineKeyboardButton(
                        "𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖", url=f"https://t.me/FH_KP"),
            ]
         ]
     )
  )

