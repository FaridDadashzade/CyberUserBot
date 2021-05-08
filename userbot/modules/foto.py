from telethon import events
from userbot.events import register as r
from random import choice as c
from userbot.cmdhelp import CmdHelp

LUCİ = ["https://telegra.ph/file/8cdc8e6b8305cc9735346.jpg", "https://telegra.ph/file/e18f95bb2a97af588c2db.jpg", "https://telegra.ph/file/94ad30d8dc078fb6ae209.jpg", "https://telegra.ph/file/dab260da8d149f246c791.jpg", "https://telegra.ph/file/4d5d38fce1e8531ed3ce6.jpg", "https://telegra.ph/file/50e2a5e422954c7b199fc.jpg", "https://telegra.ph/file/c73ce83ad7a680e98975f.jpg", "https://telegra.ph/file/26aa2b4bab017453d09da.jpg", "https://telegra.ph/file/5b65ef21c23bf10222733.jpg", "https://telegra.ph/file/32bf927222b08943ed9cd.jpg", "https://telegra.ph/file/4463244bedf6ca44aacff.jpg", "https://telegra.ph/file/0eeaf3810b2091f8efd6c.jpg", "https://telegra.ph/file/76c1f1e07e4dba167985a.jpg", "https://telegra.ph/file/4893564fdb3c5326431be.jpg", "https://telegra.ph/file/91c9b857759ffbb6d6cb8.jpg", "https://telegra.ph/file/bacd9828677b94ba1baa6.jpg", "https://telegra.ph/file/187c326f920d38ccf787e.jpg", "https://telegra.ph/file/e4fb34fd3f2c3c6b2529f.jpg","https://telegra.ph/file/8645c1a53bbdaf3c031b8.jpg", "https://telegra.ph/file/6ff090487481c848813a0.jpg,ç", "https://telegra.ph/file/67e0bc881fae7c58db0e9.jpg", "https://telegra.ph/file/baf3890e67abf7e362de1.mp4", "https://telegra.ph/file/46778abf5f09a4514f6ac.jpg", "https://telegra.ph/file/08180a881f77edd3ad334.jpg", ]

QIZ = ["https://telegra.ph/file/65024919e1d4111d34d62.jpg", "https://telegra.ph/file/ecbed0fb8fd5db9501490.jpg", "https://telegra.ph/file/00b4ef6459930ad0acf29.jpg", "https://telegra.ph/file/c589704e0c0a32de516cb.jpg", "https://telegra.ph/file/53e6a94ec0a1acf9128be.jpg", "https://telegra.ph/file/69b751c20e7c5a0f8c479.jpg", "https://telegra.ph/file/bc9bd0bf98fe400ec60e4.jpgc", "https://telegra.ph/file/e0190ff444d618e01a270.jpg", "https://telegra.ph/file/3e836a8ec96fed6706aa1.jpg", "https://telegra.ph/file/512aac384771f1d79f17b.jpg", "https://telegra.ph/file/28b77ba3acd0acdec487a.jpg", "https://telegra.ph/file/cb2303ccb0e5ff50883d0.jpg", "https://telegra.ph/file/f590aad5dba885cf53b1e.jpg", "https://telegra.ph/file/f8c51dfcc80d9a923a092.jpg", "https://telegra.ph/file/854cd58d4663d6051276e.jpg", "https://telegra.ph/file/4b06010bc839dae8765ba.jpg", "https://telegra.ph/file/ff2e8a9f5162f20a81618.jpg", "https://telegra.ph/file/cf7dce97ccbf59b471e53.jpg", "https://telegra.ph/file/631f1dded0a2d21d84f8c.jpg", "https://telegra.ph/file/45c0041d9825585cfc69b.jpg", "https://telegra.ph/file/9a39d5e18e347211eb8b4.jpg", "https://telegra.ph/file/67b9333b87ef31df2c9f1.jpg", "https://telegra.ph/file/ad44d03d73ed11c39f2be.jpgc", "https://telegra.ph/file/d9ca42940e07350d1fdc7.jpg", "https://telegra.ph/file/2b13808cc8506e499841c.jpg", "https://telegra.ph/file/287702aa21ea8b911d638.jpg", "https://telegra.ph/file/4184febfc8b611ff7fa95.jpg", "https://telegra.ph/file/81ed4f387b54cac2d3b71.jpg", "https://telegra.ph/file/62f1df52e3ae2d9541673.jpg", "https://telegra.ph/file/19d7a93817714ea6a73b3.jpg", "https://telegra.ph/file/ed2ffda37f5febf0ad544.jpg", "https://telegra.ph/file/eef8bb0fb8940d322b4bb.jpg", "https://telegra.ph/file/405eebf9aee3aa7e2f315.jpg"]

OGLAN = ["https://telegra.ph/file/8c4864b392367674ae00a.jpg", "https://telegra.ph/file/70f0a89fdaae2201974bd.jpg", "https://telegra.ph/file/0a73b6f54036f45e332e7.jpg", "https://telegra.ph/file/4ab2ad29e98725df8ec17.jpg", "https://telegra.ph/file/2eebdfac5a2386fecec31.jpg", "https://telegra.ph/file/eb71f7d6ea4805ccf6de5.jpg", "https://telegra.ph/file/3c6cf14d619bd915b60fe.jpg", "https://telegra.ph/file/114987914c564760cc71c.jpg", "https://telegra.ph/file/15d96a657ab592f9cd09a.jpg", "https://telegra.ph/file/5196bac9cd6fbfd6e6696.jpg", "https://telegra.ph/file/77908f3ab7a43b7d7282b.jpg", "https://telegra.ph/file/0f8cdfdf5acf1a1c78b60.jpg", "https://telegra.ph/file/e55b17371d53d0aeaf9ee.jpg", "https://telegra.ph/file/6af86a3bcef7923ee6e83.jpg", "https://telegra.ph/file/b107cdc4818da591dc784.jpg", "https://telegra.ph/file/acaefd13620704ffc3544.jpg", "https://telegra.ph/file/568c1bf583b2e7a46d9c4.jpg", "https://telegra.ph/file/5fe1faf66e450152bf0c1.jpg", "https://telegra.ph/file/7bbc03f00c1631e2d7c76.jpg", "https://telegra.ph/file/988e0a77eadc8cb9c1dc4.jpg", "https://telegra.ph/file/e7a4d1b6e97ad85750910.jpg"] 

@r(outgoing=True, pattern="^.foto(.*)")
async def foto(e):
	input_str = e.pattern_match.group(1).lower()
	if input_str in ["luci", "lusi"]:
		await e.client.send_file(e.chat_id, c(LUCİ))
		await e.delete()
	if input_str in ["qız", "qiz"]:
		await e.client.send_file(e.chat_id, c(QIZ))
		await e.delete()
	if input_str in ["oğlan", "oglan"]:
		await e.client.send_file(e.chat_id, c(OGLAN))
		await e.delete()

Help = CmdHelp("foto")
Help.add_info("@TheCyberUserBot rəsmi plugin.\n**💬İstifadəsi: ** `.foto` | `luci` | `qız` | `oğlan`")
Help.add_command("foto", None, "Təsadüfi oğlan və ya qız profil fotoları atar.")
Help.add_warning("Nümunə :<.fotoluci> və ya <.fotoqız> və ya <.fotooğlan>")
Help.add() 