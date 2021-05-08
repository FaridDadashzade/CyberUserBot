# CyberUserBot - Luciferxz # 
#
# Credits: https://t.me/fireqanQPlugin/112

from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from time import sleep

@register(outgoing=True, pattern="^.tag(?: |$)(.*)")
async def _(tag):

	if tag.pattern_match.group(1):
		seasons = tag.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tag.get_input_chat()
	a_=0
	await tag.delete()
	async for i in bot.iter_participants(chat):
		if a_ == 500:
			break
		a_+=5
		await tag.client.send_message(tag.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(1.4)
		
		
@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(tagadmin):
	
	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(1.4)
