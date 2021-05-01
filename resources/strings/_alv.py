# +======================================================+
# +======================================================+

alv = (
"""
**©icss - @rruuurr
  - Plugin Alive** 
  - **Commend:** `.السورس`
  - **Function:** لعرض معلومات السورس
"""
)

import time
from platform import python_version
from telethon import version
from resources.strings import *

from resources.Formation.plugins import ALIVE_NAME, icsv, mention
from resources.Formation.plugins import reply_id as rd

DEFAULTUSER = ALIVE_NAME or "ICSS"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪"
ICSEM = Config.CUSTOM_ALIVE_EMOJI or "  ⌔∮ "

_, check_sgnirts = check_data_base_heal_th()

ics_c = f"**{ICSS_TEXT}**\n"
ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 \n"
ics_c += f"**{ICSEM} قاعدة البيانات ↫** `{check_sgnirts}`\n"
ics_c += f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
ics_c += f"**{ICSEM} اصدار اڪسس ↫** `{icsv}`\n"
ics_c += f"**{ICSEM} اصدار البايثون ↫** `{python_version()}\n`"
ics_c += f"**{ICSEM} المستخدم ↫** {mention}\n"
ics_c += f"**{ICSEM} مطور السورس ↫** [اضغط هنا](t.me/rruuurr) 𓆰.\n"
ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        

def check_data_base_heal_th():
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output

# +======================================================+
# +======================================================+
