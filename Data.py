from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
⌯¦مرحبـاً بـك عزيـزي 📬 {}
⌯¦في بــوت استـخـراج جلـسـة
⌯¦استـخـراج تيرمـكـس تليثون
⌯¦وبــايــروجـرام للـمـيــوزك🎧
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة:  [⌯DEV BOT⌯](https://t.me/G5_F1)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton(text="🔙رجوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton("• DE⃟V BOT •", url="https://t.me/G5_F1"),
         InlineKeyboardButton("• قناة السورس •", url="https://t.me/Big1_Bang1") 
        ],
        [
            InlineKeyboardButton("❓¦طـريـقـه الاسـتـخـدام", callback_data="help"),
            InlineKeyboardButton("💾¦مـعـلومـات", callback_data="about")
      ],
        [InlineKeyboardButton("⚙️¦الــســـورس", url="https://t.me/Big1_Bang1")],
    ]


    # Help Message
    HELP = """
**📚¦الاوامــر الـمتـاحـه**
/about - معلومات البوت
/help - طريقه استخدامي
/start - حتى تشغل البوت
/generate - حتى تبدا بأستخراج كود
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**💾¦مـعـلومـات** 
⚡¦بـوت استخـراج كـود تيرمكـس خـاص بســورس التليـثون وكــود بـايــروجـرام خـاص بـسـورس الـمـيـوزك🎶

🌀¦قـنـاه الـبـوت : [⌯𝗦𝗢𝗨𝗥𝗖𝗘™⌯](https://t.me/Big1_Bang1)

🌏¦اللـغــه : [بـايـثـون](www.python.org)

👨🏼‍💻¦الـمـبـرمــج : @G5_F1
    """
