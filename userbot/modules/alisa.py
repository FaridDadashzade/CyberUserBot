from telethon import events
from userbot.events import register as r
from random import choice as c
from userbot.cmdhelp import CmdHelp

ÜZGÜN = ["https://telegra.ph/file/5bd5124e91b3c2e60011d.mp4", "https://telegra.ph/file/7f45601d1c4281c7ea8ad.mp4", "https://telegra.ph/file/7e1d9cb0073139efc7ef1.mp4", "https://telegra.ph/file/7292bab8a37b06d900b82.mp4", "https://telegra.ph/file/296dad84adb4d5f378b9d.mp4", "https://telegra.ph/file/658ad1a7bab23b991b133.mp4", "https://telegra.ph/file/24fd1a47500cebe672546.mp4", "https://telegra.ph/file/432ff6c2b7616f5170a08.mp4", "https://telegra.ph/file/537a5b33ee9901c04206b.mp4"]

SEVINCLI = ["https://telegra.ph/file/faabda52fafb1ab8a1aa0.mp4", "https://telegra.ph/file/e14b4ef05a70e25eff142.mp4", "https://telegra.ph/file/6426488f5c15e43c8b5aa.mp4", "https://telegra.ph/file/4a46941c3ecbeea1a813d.mp4", "https://telegra.ph/file/1597c11c8fde05dead192.mp4", "https://telegra.ph/file/b6bf457de104e2b0731c8.mp4", "https://telegra.ph/file/c9c0f773fdcc186c2df16.mp4", "https://telegra.ph/file/619d666e9387f63a3a862.mp4", "https://telegra.ph/file/99d070c9a724f3f67e296.mp4", "https://telegra.ph/file/7b179401ef830d7d708d1.mp4", "https://telegra.ph/file/53d514dd65ea94bedcea8.mp4", "https://telegra.ph/file/3abf4945c54d51719c58c.mp4", "https://telegra.ph/file/fa5653e598cd428a8f8ec.mp4", "https://telegra.ph/file/bf08e53e3c2d896692687.mp4", "https://telegra.ph/file/5cdf73c4bf04c3cdd9d95.mp4", "https://telegra.ph/file/b61fd40b4d1d64be8254a.mp4", "https://telegra.ph/file/3af84eb84f0281d5e2bdc.mp4", "https://telegra.ph/file/9f5d7bc6f96f2a04ee7a4.mp4", "https://telegra.ph/file/b7859e5f326241a85eb38.mp4", "https://telegra.ph/file/afa739d8503e67fe30e78.mp4", "https://telegra.ph/file/2fb9cabd36fe227b26987.mp4", "https://telegra.ph/file/3359f05fc2333debb4ee7.mp4", "https://telegra.ph/file/9b97e60e1285e09d53823.mp4", "https://telegra.ph/file/624320fdeba0254b956df.mp4", "https://telegra.ph/file/0dc51f5cce010e19eeee4.mp4", "https://telegra.ph/file/688e3221f1c6f86f23356.mp4", "https://telegra.ph/file/e605d97fac17e6c73d27a.mp4", "https://telegra.ph/file/76d69ec1b78c6a5f4271a.mp4", "https://telegra.ph/file/c093602f2ef193e50a498.mp4", "https://telegra.ph/file/70b396d1b50229f0d1d98.mp4", "https://telegra.ph/file/e6ddfdcc87aefd94c9235.mp4", "https://telegra.ph/file/781c36b1eaa3a1f11118c.mp4", "https://telegra.ph/file/c5b3ae879644306f4ce87.mp4", "https://telegra.ph/file/9523c2a21f725abf9bce1.mp4", "https://telegra.ph/file/5022ea344c5cbb6e4fced.mp4", "https://telegra.ph/file/10714acfee97a1106845c.mp4", "https://telegra.ph/file/7d4dda3da9563331448b3.mp4", "https://telegra.ph/file/ad779fa795a3d18ca4f03.mp4"]

ESEBI = ["https://telegra.ph/file/aee38d44d74c6d6157020.mp4", "https://telegra.ph/file/264e484b4efc704e6e0ea.mp4", "https://telegra.ph/file/b2e530263339b24423d81.mp4", "https://telegra.ph/file/d12aa4a5471c9864a72c6.mp4"]

TEECCUBLENMIS = ["https://telegra.ph/file/5dcef6280aa6cdb28bcf8.mp4", "https://telegra.ph/file/1146389f45b9d7be28a3a.mp4", "https://telegra.ph/file/f1123e45d62c0616636cf.mp4", "https://telegra.ph/file/17c30b1d01a0723ed5dd9.mp4", "https://telegra.ph/file/ee3858960cbfd6aa8ffb9.mp4", "https://telegra.ph/file/5adc5175a5ff88835c5ac.mp4", "https://telegra.ph/file/e190cc6df1111e83078c2.mp4", "https://telegra.ph/file/fc21ac7ad1f34f98fc8ab.mp4", "https://telegra.ph/file/9741b0861b2e3698bd2a7.mp4", "https://telegra.ph/file/92f68fca1eacba80fd620.mp4", "https://telegra.ph/file/feb442cd943a0c7fe4b29.mp4", "https://telegra.ph/file/fe2547dfd881f546f1319.mp4", "https://telegra.ph/file/3df9216633a25be84c2cd.mp4"]

AC = ["https://telegra.ph/file/876efb633cafcb640a8d4.mp4", "https://telegra.ph/file/7a396f0b2cbfe26989077.mp4", "https://telegra.ph/file/f3a0ea1d069201467c2b0.mp4", "https://telegra.ph/file/8ef83f39514f092cc4c2d.mp4", "https://telegra.ph/file/efa722e71b69d27ce6f0a.mp4", "https://telegra.ph/file/cb25fbe354fb2831dbb19.mp4", "https://telegra.ph/file/76519dc00d9a515fd45b4.mp4", "https://telegra.ph/file/418fe58648ab597cd03ce.mp4", "https://telegra.ph/file/fa49afe2c34730a17b4f4.mp4", "https://telegra.ph/file/1b38937b5a6a729869e7b.mp4", "https://telegra.ph/file/d8a1bf8529b2c850b0ba4.mp4"]

ÇALIŞQAN = ["https://telegra.ph/file/db5fbf815a1973c843c47.mp4", "https://telegra.ph/file/ee39cb53f68eaf851c910.mp4", "https://telegra.ph/file/7aeffdf54a46e2574d663.mp4", "https://telegra.ph/file/01492bbc405e1200991d8.mp4", "https://telegra.ph/file/84cbaadb624033cd8a467.mp4", "https://telegra.ph/file/551621489ab0eaa90425c.mp4"]

YUXULU = ["https://telegra.ph/file/f546a158cc9aa955333dd.mp4", "https://telegra.ph/file/b59042e4b99574f9469ac.mp4", "https://telegra.ph/file/134b7b568559ab502f952.mp4", "https://telegra.ph/file/e3c451d477c82264939ed.mp4", "https://telegra.ph/file/06f54e2d990f8e83a0460.mp4", "https://telegra.ph/file/309609f2df9fe6917a719.mp4"]

@r(outgoing=True, pattern="^.alisa (.*)")
async def alisa(e):
	input_str = e.pattern_match.group(1).lower()
	if input_str in ["üzgün", "uzgun"]:
		await e.client.send_file(e.chat_id, c(ÜZGÜN))
		await e.delete()
	if input_str in ["sevincli"]:
		await e.client.send_file(e.chat_id, c(SEVINCLI))
		await e.delete()
	if input_str in ["əsəbi", "esebi", "əsebi", "esəbi"]:
		await e.client.send_file(e.chat_id, c(ESEBI))
		await e.delete()
	if input_str in ["təəccüblənmiş", "teeccublenmis", "təəccüblenmis", "təəccüblənmiş", "təəccüblənmiş", "təəccüblənmiş", "təəccüblənmiş"]:
		await e.client.send_file(e.chat_id, c(TEECCUBLENMIS))
		await e.delete()
	if input_str in ["ac"]:
		await e.client.send_file(e.chat_id, c(AC))
		await e.delete()
	if input_str in ["çalışqan", "calisqan"]:
		await e.client.send_file(e.chat_id, c(ÇALIŞQAN))
		await e.delete()
	if input_str in ["yuxulu"]:
		await e.client.send_file(e.chat_id, c(YUXULU))
		await e.delete()

Help = CmdHelp("alisa")
Help.add_info("@Luciferxz tərəfindən hazırlanmışdır\n**💬İstifadəsi: ** `.alisa` `üzgün` | `sevincli` | `əsəbi` | `təəccüblənmiş` | `ac` | `çalışqan` | `yuxulu`")
Help.add_command("alisa", None, "Təsadüfi bir alisa gif-i atar.")
Help.add()