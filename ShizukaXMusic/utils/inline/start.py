import asyncio
import re
import os
import random
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from typing import Union
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from ShizukaXMusic import app
from strings.filters import command

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"",
            ),
            InlineKeyboardButton(
                text=_["S_B_S"], callback_data="amm"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(

                    text=_["S_B_9"], url=f"https://t.me/UIU_II"

                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], url=f"https://t.me/UIU_II"
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_12"], url=f"https://t.me/UIU_II"

                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_10"], url=f"https://t.me/UIU_II"

                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons





  
  
REPLY_MESSAGE = "- اهلين ياحلو عندك الازرار تحت استمتع"

REPLY_MESSAGE_BUTTONS = [
         [
             ("طريقة تشغيل ليندا"),                   
             ("اوامر ليندا")

          ],
          [             
             ("&اوامر التسليه&")
          ],
          [
             ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & filters.command("commands"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.regex("اخفاء الازرار") & filters.private)
async def down(client, message):
          m = await message.reply("**- ابشر ياحلو تم اخفاء الازرار بنجاح\n- لو تبي تظهرها مرة ثانية ارسل**-› /commands", reply_markup= ReplyKeyboardRemove(selective=True))
########رسائل الستارت########

@app.on_message(filters.private & command("طريقة تشغيل ليندا"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياحلو عشان تفعل بوت ليندا اتبع الخطوات الي بالاسفل**

1.) **اولا قم بإضافة البوت اللي مجموعتك \n√.**
2.) **قم برفع البوت مشرف مع الصلاحيات المطلوبة \n√.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر \n√.**
4.) **تاكد من تشغيل المحادثة الصوتية\n√.**
5.) ** اكتب شغل او تشغيل + اسم الاغنية \n√.**
▪️ ** في حال لم يستطع الحساب المساعد الانضمام إلى مجموعتك قم باضافتة يدوي\n√.**
\n√ **في حال واجهت اي مشكلة اخرى يمكنك التواصل معي : @FH_ME **
\n __ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 [ᴄʜᴀɴɴᴇʟ](https://t.me/KB_HE)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس ليندا ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**

مطور السورس -› [devpokemon](t.me/devpokemon)
قناة السورس -› [᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ](t.me/UIU_II)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

###################new lian#############

REPLY_MESSAGEE = "- هلا فيك في قسم الاوامر"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & command("اوامر ليندا"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("رجوع"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("شرح التشغيل بمنصات الاغاني"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓

• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify

- بتلقى شرح لكل هالمنصات في المجموعة اكتب فقط م الاوامر**

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("اوامر المجموعة"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f""" ◍ - اوامر تشغيل البوت في المجموعات - √

◍ -『 **تشغيل او شغلي** 』\n ثم اسم الاغنية او بالرد على ملف صوتي •
◍ -『 **ايقاف او انهاء** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه •
◍ -『 **تخطي او التالي** 』\n  للتخطي إلي الاغنيه المنتظر بقائمة الانتظار لديك •
◍ -『 ** /restart ** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("اوامر القنوات"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f""" - ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القنوات  •

◍ -『 **/cplay** 』\n ثم اسم الاغنية او بالرد على ملف صوتي •
◍ -『 **/cpause** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •
◍ -『 **/cresume** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •
◍ -『 **/cmute** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **/cunmute** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **/cskip** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •
◍ -『 **cstop** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •
\n\n╰── • [sᴏᴜʀᴄᴇ sᴇᴢᴀʀ](t.me/UIU_II) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("طريقة البحث"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓

[ بحث او يوت + اسم المطلوب ..]

مثال -› بحث بحبك وحشتني

- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- اهلين ياحلو •
1 » خطوات تشغيل في القناه •

2 » لتشغيل في قناتك •

3 ‌‏« قم بانشاء جروب مربوط بقناتك •

4 » تقوم باضافة البوت في القناتك و مجموعتك وترفعه مشرف •

5 » لربط القناتك بالمجموعه ارسل  الامر التالي في المجموعة •
            
6 » /channelplay + معرف قناتك •

7 » /channelplay @FH_KP مثـل •**

8 » **للاستفسار** » @FH_KN""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لمجموعتك •", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
