"""
CYBERUSERBOT 
LUCIFERXZ
"""
from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp 
from userbot import CYBER_VERSION
from time import sleep

@register(outgoing=True, pattern="^.tag(?: |$)(.*)")
async def tagger(cyber):
	if cyber.fwd_from:
		return

	if cyber.pattern_match.group(1):
		seasons = cyber.pattern_match.group(1)
	else:
		seasons = ""

	chat = await cyber.get_input_chat()
	a_=0
	await cyber.delete()
	async for i in bot.iter_participants(chat):
		if a_ == 5000:
			break
		a_+=1
		await cyber.client.send_message(cyber.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(1)


@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(cyber):
	if cyber.fwd_from:
		return
	

	if cyber.pattern_match.group(1):
		seasons = cyber.pattern_match.group(1)
	else:
		seasons = ""

	chat = await cyber.get_input_chat()
	a_=0
	await cyber.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 5000:
			break
		a_+=1
		await cyber.client.send_message(cyber.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(1)

Help = CmdHelp('tag')
Help.add_command('tag <səbəb>', None, 'Qrupdakı istifadəçiləri tag edər. ')
Help.add_command('alladmin <səbəb>', None, 'Bütün adminləri tag edər.')
Help.add_command('restart', None, 'Tag etməni dayandırar.')
Help.add_info('@Luciferxz tərəfindən @TheCyberUserBot üçün hazırlanıb.')
Help.add()	
