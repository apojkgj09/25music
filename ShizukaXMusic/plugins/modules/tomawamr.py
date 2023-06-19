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


@app.on_message(filters.command(["تفعيل"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3e46bfad79e017c69ff69.jpg",
caption=f"""**- اهلين ياحلو  {message.from_user.mention}\n\n شكرآ لاستضافتي الي مجموعتك**\n\n **انا بوت  اختصاصـي  تشغيل الاغاني في المحادثه الصوتيه**\n\n **لمعرفة كيفة استخدامي وطريقة التشغيل اضغط على زر بأسفل 👇**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                
                    InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data="arbic"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("arbic"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""**• انا بوت اختصاصـي  تشغيل الأغاني في المحادثات الصوتيـه بـدون تقطيع **\n\n**إذا واجهت مشكله تواصل مع مطور البوت** @FHK_M5\n\n ~ **جميع اوامر البوت موجودة بالاسفل👇**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data=f"mmmm"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"zzzz"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"pppp"),

                ],[
                    InlineKeyboardButton(
                        "التحديثات", url=f"https://t.me/FH_KP"),

                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/FHK_M5"),
                ],[
                    InlineKeyboardButton(
                        "أضفني لمجموعتك", url=f"https://t.me/LANDHLBOT?startgroup=true"),

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("mmmm"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""**طريقة تفعيل البوت في مجموعتك :**
1 - **اولا قم بإضافة البوت اللي مجموعتك \n√.**
2 - **قم برفع البوت مشرف مع الصلاحيات المطلوبة \n√.**
3 - ** لتحديث قائمة الادمن /Reload قم بكتابة الامر \n√.**
4 - **تاكد من تشغيل المحادثة الصوتية\n√.**
5 - ** اكتب شغل او تشغيل + اسم الاغنية \n√.**
6 - ** في حال لم يستطع الحساب المساعد الانضمام إلى مجموعتك قم باضافتة يدوي\n√.**
\n√ **في حال واجهت اي مشكلة اخري يمكنك التواصل معي : @FH_ME **
\n __ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 [ᴄʜᴀɴɴᴇʟ](https://t.me/KB_HE)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [                  
                   
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"arbic"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("pppp"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القناه**


1 - لتشغيل اغنيه اكتب : /cplay
2 - لتشغيل فيديو اكتب : /cvideo
3 - لأنهاء الاغنيه اكتب : /cstop
4 - لايقاف الاغنيه مؤقت اكتب : /cpause
5 - لتكملة الاغنيه من الايقاف المؤقت اكتب :/cresume
6 - لتخطي الاغنيه اكتب : /cskip
7 - لكتم البوت في الكول اكتب : /cmute
8 - لألغاء كتم البوت في الكول اكتب : /cunmute""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [                  
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"yyyy"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"arbic"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("yyyy"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القناه**    

1 » خطوات تشغيل في القناه

2 » لتشغيل في قناتك

3 ‌‏« قم بانشاء جروب مربوط بقناتك

4 » تقوم باضافة البوت في القناتك و مجموعتك وترفعه مشرف

5 » لربط القناتك بالمجموعه ارسل  الامر التالي في المجموعة
            
6 » /channelplay + معرف قناتك

7 » /channelplay @FH_KP مثـل**..

8 » **للاستفسار** » @FH_KN""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [                                 
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"arbic"),
               ],
          ]
        ),
    ) 

@app.on_callback_query(filters.regex("zzzz"))
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
                        "رجـوع 🎶", callback_data=f"arbic"),
               ],
          ]
        ),
                    )
