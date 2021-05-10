from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
import os

fayl_adi=0
@register(outgoing=True, pattern="^.pyarat (.*) (.*) (edit|alt|foto|musiqi)$")
async def _(pyarat):
	global fayl_adi
	if pyarat.is_reply:
		mesaj = await pyarat.get_reply_message()
		name = pyarat.pattern_match.group(1)
		sleep_t = pyarat.pattern_match.group(2)
		sec = pyarat.pattern_match.group(3)

		if name == "":
			await pyarat.edit("**Xahiş edirəm bir əmr qeyd edin...**")
			return

		else:
			if sleep_t == "":
				await pyarat.edit("**Xahiş edirəm plugin sürətini qeyd edin....**")
				return

			else:
				if sec == "":
					await pyarat.edit("**Bəzi məlumatlar çatışmır...**")
					return

				else:
					if sec.lower() == "edit":
						siyahi=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							siyahi.append(i)
						fayl_adi=fayl_adi+1

						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.e_(fayl_adi, name, slep, siyahi)
						await pyarat.client.send_file(pyarat.chat_id, f"./cyberuserbot{fayl_adi}.py", force_document=True, caption="Bu plugin @TheCyberUserBot ilə hazırlanmışdır...")
						await pyarat.delete()
						os.remove(f"./cyberuserbot{fayl_adi}.py")
						return

					if sec.lower() == "alt":
						siyahi=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							siyahi.append(i)
						fayl_adi=fayl_adi+1

						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.a_(fayl_adi, name, siyahi, slep)
						await pyarat.client.send_file(pyarat.chat_id, f"./cyberuserbot{fayl_adi}.py", force_document=True, caption="Bu plugin @TheCyberUserBot ilə hazırlanmışdır...")
						await pyarat.delete()
						os.remove(f"./cyberuserbot{fayl_adi}.py")
						return

					if sec.lower() =="foto":
						siyahi=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							siyahi.append(i)
						fayl_adi=fayl_adi+1
						slep = sleep_t if sleep_t else 1.6
						import userbot.helpers.p as edit
						edit.r_(fayl_adi, name, siyahi)
						await pyarat.client.send_file(pyarat.chat_id, f"./cyberuserbot{fayl_adi}.py", force_document=True, caption="Bu plugin @TheCyberUserBot ilə hazırlanmışdır...")
						await pyarat.delete()
						os.remove(f"./cyberuserbot{fayl_adi}.py")
						return

					if sec.lower() in ["musiqi"]:
						siyahi=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							siyahi.append(i)
						fayl_adi=fayl_adi+1
						import userbot.helpers.p as edit
						edit.m_(fayl_adi, name, siyahi)
						await pyarat.client.send_file(pyarat.chat_id, f"./cyberuserbot{fayl_adi}.py", force_document=True, caption="Bu plugin @TheCyberUserBot ilə hazırlanmışdır...")
						await pyarat.delete()
						os.remove(f"./cyberuserbot{fayl_adi}.py")
						return


					

					else:
						await pyarat.edit("**Bağışlayın, xəta baş verdi....**")
						return



	else:
		await pyarat.edit("**Bir mesaja yanıt verməlisən!**")
		return

Help = CmdHelp("pyarat")
Help.add_command("pyarat", "<pluginin_əmri> <plugin_sürəti> <edit/alt/foto/musiqi> ", "@TheCyberUserBot sizin üçün plugin yaradar...")
Help.add()
