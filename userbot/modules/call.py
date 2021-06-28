# CYBERUSERBOT - FARID DADASHADE
#
# THANKS: https://github.com/TamilBots/TamilUserBot/blob/master/userbot/plugins/GroupCall.py


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from userbot.events import register
from userbot import bot, get_call
from userbot.cmdhelp import CmdHelp


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@register(outgoing=True, groups_only=True, pattern="^.vcbaslat$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit("`Bunu etmək üçün admin olmalıyam!`")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Səsli söhbət başladı!`")
    except Exception as ex:
        await c.edit(f"Bir xəta baş verdi\nXəta: `{ex}`")


@register(outgoing=True, groups_only=True, pattern="^.vcbagla$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit("`Bunu etmək üçün admin olmalıyam!`")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Səsli söhbət uğurla sonlandırıldı!`")
    except Exception as ex:
        await c.edit(f"Bir xəta baş verdi\nXəta: `{ex}`")



@register(outgoing=True, groups_only=True, pattern="^.tagvc")
async def _(c):
    await c.edit("`İstifadəçilər səsli söhbətə çağrılır...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    cyber = list(user_list(users, 6))
    for p in cyber:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"`{z}` **istifadəçi çağırıldı...**")


CmdHelp('VoiceChat').add_command(
    'vcbaslat', None, 'Bir qrupda səsli söhbət başladar.'
).add_command(
    'vcbagla', None, 'Səsli söhbəti sonlandırar.'
).add_command(
    'tagvc', None, 'Qrupdaki istifadəçiləri səsli söhbətə dəvət edər.'
).add()
