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



REPLY_MESSAGE = "- اهلين ياحلو تحكم من الازرار اسفل"




REPLY_MESSAGE_BUTTONS = [

         ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("افتار عيال"),
        ("افتار بنات")
    ],
    [
        ("قران")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
    ],
    [
       ("انصحني. 🥲")
        
    ],
    [ 
              
      ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.command(["اوامر التسليه"],""))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب ميرا**", reply_markup= ReplyKeyboardRemove(selective=True))
