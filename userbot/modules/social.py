# TheCyberUserBot - Luciferxz
# Forked by SpaceUserBot - @TheMiri
#
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import bot

@register(outgoing=True, pattern="^.pint ?(.*)")
@register(outgoing=True, pattern="^.tik ?(.*)")
@register(outgoing=True, pattern="^.inst ?(.*)")
async def spaceinsta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Yükləmək üçün bir linki yanıtlayın.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Yükləmək üçün bir linki yanıtlayın.`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Sender istifadəçini tapmadığı üçün script dayandırıldı.")
        return
    asc = await event.edit("`Yüklənir...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit(" @SaveAsBot `blokdan çıxardın və bir daha yenidən yoxlayın`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Gizlilik ayarlarınızdakı ileti qismini düzəldin."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"`@TheCyberUserBot ilə yükləndi`",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            
@register(outgoing=True, pattern="^.dzl(?: |$)(.*)")
async def SpaceDeez(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await event.edit("`Yükləmək üçün linkə ehtiyacım olduğunu bilirsən`")
    else:
        await event.edit("**Yükləmə başladııdı** 🎶")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(dlink)
              details = await conv.get_response()
              song = await conv.get_response()
#                                   #
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.edit("@DeezLoadBot'u blokdan çıxardın və bir daha yenidən yoxlayın.")
              return
          await bot.send_file(event.chat_id, song, caption=details.text)
          await event.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, details.id, song.id])
          await event.delete()     
          
CmdHelp('social').add_command(
    'inst', '<link>', 'Instagramdan post yükləyər.'
).add_command(
    'tik', '<link>', 'Cavap verdiyiniz linkdən tiktok postunu tapar və göndərər.'
).add_command(
    'pint', '<link>', 'Cavab verdiyiniz Pinterest linkindən postu tapar və media olaraq göndərər.'
).add_command(
    'dzl', '<link>', 'Verdiyiniz spotify/deezer linkini musiqi olarağ atar.'
).add()
