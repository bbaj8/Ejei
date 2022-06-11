from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 ابد بتوليد الجلسه 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ قناه البوت ✨", url="https://t.me/R125R")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
    ]

    START = """
يا {}

مرحبا بك في {}

إذا كنت لا تثق بهذا الروبوت ،
1) التوقف عن قراءة هذه الرسالة
2) حذف هذه الدردشة

لا أزال أقرأ؟
يمكنك استخدامي لإنشاء pyrogram (حتى الإصدار 2) وجلسة telethon string. استخدم الأزرار أدناه لمعرفة المزيد
    """

    HELP = """
✨ **Available Commands** ✨

/about - حول الروبوت 
/help - هاي الرساله
/start - بدا البوت
/generate - استخراج
/cancel - الغاء عمليه
/restart - اعادة تشغيل 
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Developer : @R125R
    """
