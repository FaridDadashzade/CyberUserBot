def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./cyberuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events

a={siyahi}

@register(outgoing=True, pattern="^.{name}$")
async def _(cyber):
	for i in a:
		await cyber.edit(' '+str(i))
		sleep({slep})

Help = CmdHelp("cyberuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @TheCyberUserbot ilə hazırlanmışdır...")
Help.add()
								""")
	return f.close()

def a_(fayl_adi, name, siyahi, slep):
	f = open(f"./cyberuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events

a={siyahi}

@register(outgoing=True, pattern="^.{name}$")
async def _(cyber):
	text= " "
	for i in a:
		text+=i+"\\n"
		await cyber.edit(text)
		sleep({slep})

Help = CmdHelp("cyberuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @TheCyberUserbot ilə hazırlanmışdır...")
Help.add()
								""")
	return f.close()

def r_(fayl_adi, name, siyahi):
	f = open(f"./cyberuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from random import choice

a={siyahi}

@register(outgoing=True, pattern="^.{name}$")
async def _(cyber):
	random_ = choice(a)
	await cyber.client.send_file(cyber.chat_id, random_)
	await cyber.delete()

Help = CmdHelp("cyberuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @TheCyberUserbot ilə hazırlanmışdır...")
Help.add()

		""")

def m_(fayl_adi, name, siyahi):
	f = open(f"./cyberuserbot{fayl_adi}.py", "x")
	f.write("""from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import random
import os

IFACI = [{siyahi}]

@register(outgoing=True, pattern="^.{name}$")
async def cybermusic(cyber):
    
    
    await cyber.edit("`Sizin üçün təsadüfi bir "+IFACI+" musiqisi axtarıram...`")

    try:
        results = await cyber.client.inline_query('deezermusicbot', '+IFACI+')
    except:
            await cyber.edit("`Bağışlayın, botdan cavab ala bilmədim!`")
            return

    netice = False
    while netice is False:
            rast = random.choice(results)
            if rast.description == IFACI:
                await cyber.edit("`Musiqi yüklənir!\nBiraz gözləyin...`")
                yukle = await rast.download_media()
                await cyber.edit("`Yüklənmə tamamlandı!\nFayl göndərilir...`")
                await cyber.client.send_file(cyber.chat_id, yukle, caption="@TheCyberUserbot sizin üçün `"+rast.description+" - "+rast.title+"` musiqisini seçdi\n\nXoş dinləmələr :)")
                await event.delete()
                os.remove(yukle)
                netice = True

Help = CmdHelp("cyberuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @TheCyberUserBot Tərəfindən Hazırlanmışdır..")
Help.add()

		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))
