# Copyright (C) 2021 FaridDadashzade.
#
# CyberUserBot - FaridDadashzade
# All rights reserved.

""" Yükləyərkən xəta verən digər userbotların pluginlərini yükləmək üçün hazırlanmışdır. """

import re
import os
from telethon.tl.types import DocumentAttributeFilename, InputMessagesFilterDocument
import importlib
import time
import traceback

from userbot import bot, tgbot, PATTERNS
from userbot.events import register
from userbot.main import extractCommands
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern="^.pfix")
@register(outgoing=True, pattern="^.pduzelt")
async def pduzelt(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.edit("Hazırlaya bilməyim üçün bir pluginə cavab verin!")
        return

    await event.edit("Plugin yüklənir...")
    fayl = await event.client.download_media(reply_message)
    dosy = open(fayl, "r").read()

    other1 = r"(from userbot import DTO_VERSION)"
    other2 = r"(from userbot import BREND_VERSION)"
    other3 = r"(from userbot import EPİC_VERSION)"

    if re.search(other1, dosy):
        await event.edit("Plugin hazırlanır..")
        emr = re.findall(other1, dosy)

        if len(emr) > 1:
            await event.edit("Bilinməyən xəta baş verdi.")

        komut = emr[0][1]
        deyisdir = dosy.replace('from userbot import DTO_VERSION', 'from userbot import CYBER_VERSION')
        deyisdir = deyisdir.replace("from userbot import BREND_VERSION", "from userbot import CYBER_VERSION")
        deyisdir = deyisdir.replace("from userbot import EPİC_VERSION", "from userbot import CYBER_VERSION")
        ported = open(f'cyber_{fayl}', "w").write(deyisdir)

        await event.edit("Hazırlanır..")

        await event.client.send_file(event.chat_id, f"cyber_{fayl}")
        os.remove(f"cyber_{fayl}")
        os.remove(f"{fayl}")
    elif re.search(other2, dosy):
        await event.edit("Plugin hazırdır..")
        emr = re.findall(other2, dosy)

        if len(emr) > 1:
            await event.edit("Bilinməyən xəta baş verdi..")
            return

        komut = emr[0][1]

        deyisdir = dosy.replace('from userbot import DTO_VERSION', 'from userbot import CYBER_VERSION')
        deyisdir = deyisdir.replace("from userbot import BREND_VERSION", "from userbot import CYBER_VERSION")
        deyisdir = deyisdir.replace("from userbot import EPİC_VERSION", "from userbot import CYBER_VERSION")
        ported = open(f'cyber_{fayl}', "w").write(deyisdir)
        ported = open(f'cyber_{fayl}', "w").write(deyisdir)

        await event.edit("Hazırlanır..")

        await event.client.send_file(event.chat_id, f"cyber_{fayl}")
        os.remove(f"cyber_{fayl}")
        os.remove(f"{fayl}")
    elif re.search(other3, dosy):
        await event.edit("Göndərilir...")
        emr = re.findall(other3, dosy)

        if len(emr) > 1:
            await event.edit("Bilinməyən xəta baş verdi..")
            return

        komut = emr[0][1]

        deyisdir = dosy.replace('from userbot import DTO_VERSION', 'from userbot import CYBER_VERSION')
        deyisdir = deyisdir.replace("from userbot import BREND_VERSION", "from userbot import CYBER_VERSION")
        deyisdir = deyisdir.replace("from userbot import EPİC_VERSION", "from userbot import CYBER_VERSION")
        ported = open(f'cyber_{fayl}', "w").write(deyisdir)

        ported = open(f'cyber_{fayl}', "w").write(deyisdir)

        await event.edit("Hazırlanır...")

        await event.client.send_file(event.chat_id, f"cyber_{fayl}")
        os.remove(f"cyber_{fayl}")
        os.remove(f"{fayl}")

    else:
        await event.edit("Bilinməyən xəta baş verdi..")
        
Help = CmdHelp('pfix')
Help.add_command('pfix', None, 'Yükləyərkən xəta verən digər userbotların pluginlərini yükləmək üçün hazırlanmışdır.')
Help.add()
