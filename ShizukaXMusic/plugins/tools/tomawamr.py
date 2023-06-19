import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)





@app.on_callback_query(filters.regex("arbic"))
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/dc6751255ec8481ace945.mp4",
        caption=f""" اهلين فيك في اوامر بوت ليندا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [                    
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"gg"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"kk"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"chua"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("hmaya"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" اهلين فيك في اوامر بوت ليندا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"gg"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"kkk"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("g1"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""""**طريقة تفعيل البوت في مجموعتك :**
1.) **اولا قم بإضافة البوت اللي مجموعتك \n√.**
2.) **قم برفع البوت مشرف مع الصلاحيات المطلوبة \n√.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر \n√.**
4.) **تاكد من تشغيل المحادثة الصوتية\n√.**
5.) ** اكتب شغل او تشغيل + اسم الاغنية \n√.**
▪️ ** في حال لم يستطع الحساب المساعد الانضمام إلى مجموعتك قم باضافتة يدوي\n√.**
\n√ **في حال واجهت اي مشكلة اخري يمكنك التواصل معي : @FH_ME **
\n __ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 [ᴄʜᴀɴɴᴇʟ](https://t.me/KB_HE)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [                  
                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("gg"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""اهلـين حبـي  أليـك قائمة اوامـر التشغيل:**
1»**لتشغيل اغنيه اكتب : تشغيل او شغل**
2»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
3»**لايقاف الاغنيه مؤقت اكتب : قفي**
4»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
5»**لتخطي الاغنيه اكتب : تخطي او التالي**
6»**لكتم البوت في المحادثه اكتب : اسڪتي**
7»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
8»**لتحميـل الاغانـي اڪتب : بحث او تحميل**
""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [                  
                                   
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("kkk"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القنوات**:
1 - لتشغيل اغنيه اكتب : /cplay
2 - لتشغيل فيديو اكتب : /cvideo
3 - لأنهاء الاغنيه اكتب : /cstop
4 - لايقاف الاغنيه مؤقت اكتب : /cpause
5 - لتكملة الاغنيه من الايقاف المؤقت اكتب :/cresume
6 - لتخطي الاغنيه اكتب : /cskip
7 - لكتم البوت في المحادثه اكتب : /cmute
8 - لألغاء كتم البوت في المحادثه اكتب : /cunmute""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [                  
                    InlineKeyboardButton(
                        "تحديثات لينـدا", callback_data=f"chua"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    ) 
@app.on_callback_query(filters.regex("chua"))
async def br(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""طريقة ربط البوت بالقناة:**
1 » خطوات تشغيل في القناه

2 » لتشغيل في قناتك

3 ‌‏« قم بانشاء جروب مربوط بقناتك

4 » تقوم باضافة البوت في القناتك و مجموعتك وترفعه مشرف

5 » لربط القناتك بالمجموعه ارسل  الامر التالي في المجموعة
            
6 » /channelplay + معرف قناتك

7 » /channelplay @FH_KP مثـل**..

8 » **للاستفسار** » @FH_KN
\n __ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 [ᴄʜᴀɴɴᴇʟ](https://t.me/KB_HE)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("رجـوع", callback_data="arbic")]]
        ),
    )
