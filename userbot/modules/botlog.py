# Copyright 2021 (C) FaridDadashzade
#
# CyberUserBot - Faridxz
# 
# oğurlayan peysərdi #

import asyncio
from userbot.events import register
from userbot import BOTLOG_CHATID, BOTLOG

@register(outgoing=True, incoming=True, func=lambda e: e.mentioned)
async def ltgm(event):
    hmm = await event.get_chat()
        
    if BOTLOG_CHATID:
        sender = await event.get_sender()
        await asyncio.sleep(5)
        if not event.is_private and not (await event.get_sender()).bot:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#TAG \n<b>Mesajı göndərən : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
			\n<b>Qrup : </b><code>{hmm.title}</code>\
                        \n<b>Mesaj : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                parse_mode="html",
                link_preview=True,
            )
            e = await event.client.get_entity(int(BOTLOG_CHATID))
            fwd_message = await event.client.forward_messages(
                    e,
                    event.message,
                    silent=True
                )
        else:
            if event.is_private:
                if not (await event.get_chat()).bot:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"#TAG \n<b>Mesajı göndərən : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
                                \n<b>ID : </b><code>{sender.id}</code>",
                        parse_mode="html",
                        link_preview=True,
                    )
                    e = await event.client.get_entity(int(BOTLOG_CHATID))
                    fwd_message = await event.client.forward_messages(
                            e,
                            event.message,
                            silent=True
                        )
