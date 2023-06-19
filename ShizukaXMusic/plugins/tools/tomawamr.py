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



@app.on_message(filters.command(["تفعيل"],""))
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/dc6751255ec8481ace945.mp4",
        caption=f""" **- اهلين ياحلو  {message.from_user.mention}\n\n شكرآ لاستضافتي الي مجموعتك لمعرفة كيفة استخدامي وطريقة التشغيل اضغط على زر بأسغل 👇**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                
                    InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data="arbic"),
                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("FH_KN"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" **- اهلين ياحلو  {message.from_user.mention}\n\n شكرآ لاستضافتي الي مجموعتك لمعرفة كيفة استخدامي وطريقة التشغيل اضغط على زر بأسغل 👇**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                
                    InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data="arbic"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""""**طريقة تفعيل البوت في مجموعتك :**
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
                        "المجموعات", callback_data=f"cAfyon"),

                    InlineKeyboardButton(
                        "القنوات", callback_data=f"cbbasic"),

                ],[
                    InlineKeyboardButton(
                        "التحديثات", url=f"https://t.me/FH_KN"),

                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/FHK_M5"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"FH_KN"),                    
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cAfyon"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""اهلـين حبـي  أليـك قائمة اوامـر التشغيل:**
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
            [[InlineKeyboardButton("🔙 رجـوع", callback_data="arbic")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""اهلـين حبـي  أليـك قائمة اوامـر التشغيل في القنوات**:
1 - لتشغيل اغنيه اكتب : /cplay
2 - لتشغيل فيديو اكتب : /cvideo
3 - لأنهاء الاغنيه اكتب : /cstop
4 - لايقاف الاغنيه مؤقت اكتب : /cpause
5 - لتكملة الاغنيه من الايقاف المؤقت اكتب :/cresume
6 - لتخطي الاغنيه اكتب : /cskip
7 - لكتم البوت في المحادثه اكتب : /cmute
8 - لألغاء كتم البوت في المحادثه اكتب : /cunmute
""",
        reply_markup=InlineKeyboardMarkup(
          [
               [                  
                    InlineKeyboardButton(
                        "ربط القناة", callback_data=f"Afyon"),
                ],[
                    InlineKeyboardButton(
                        "🔙 رجـوع.", callback_data=f"arbic"),
               ],
          ]
        ),
    )




@Client.on_callback_query(filters.regex("Afyon"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**طريقة ربط البوت بالقناة:**
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
            [[InlineKeyboardButton("•رجـوع•", callback_data="arbic")]]
        ),
    )
