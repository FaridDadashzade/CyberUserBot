def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./cyberuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from userbot import CYBER_VERSION
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
from userbot import CYBER_VERSION
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
from usertbot import CYBER_VERSION
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
	f.write("""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from userbot import CYBER_VERSION
import random
import os

IFACILAR = [{siyahi}]
IFACI = (IFACILAR[0])

@register(outgoing=True, pattern="^.{name}$")
async def _(cyber):
    musiqi = random.choice(IFACILAR)
    await cyber.edit("`"+IFACILAR+" axtarıram...`")

    try:
        try:
            sonuclar = await cyber.client.inline_query('deezermusicbot '+IFACI+' '+musiqi)
        except:
            await cyber.edit("`Bağışlayın, botdan cavab ala bilmədim!`")
            return

        true_but_false = True
        while true_but_false == True:
            rast = random.choice(sonuclar)
            if rast.description == IFACI:
                await cyber.edit("`Musiqi yüklənir! Biraz gözləyin...`")
                indir = await rast.download_media()
                await cyber.edit("`Yüklənmə tamamlandı! Fayl göndərilir...`")
                await cyber.client.send_file(cyber.chat_id, indir, caption="@TheCyberUserbot Sənin üçün `"+rast.description+" - "+rast.title+"` Seçdi\\n\\nXoş dinləmələr :)")
                await event.delete()
                os.remove(indir)
                true_but_false=False

    except:
        cyber.edit("Musiqini tapa bilmədim!")
        return

Help = CmdHelp("cyberuserbot{dosya_name}")
Help.add_command("{name}", None, "Bu Plugin @TheCyberUserBot Tərəfindən Hazırlanmışdır..")
Help.add()

		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))
