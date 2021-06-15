# Copyright (C) 2021 Farid Dadashzade.
#
# All rights reserved.

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot.cmdhelp import CmdHelp
from userbot import BOTLOG, BOTLOG_CHATID, bot
from userbot.events import register as cyber



@cyber(outgoing=True, pattern=r"^\.sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    cyber = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await cyber.delete()

    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "`Özünü məhv edən mesaj göndərildi və silindi...`")

CmdHelp('mesaj').add_command(
    'sd', '<vaxt + mesaj>', 'Yazdığınız mesajı qeyd etdiyiniz vaxt ərzində silər.'
).add()
