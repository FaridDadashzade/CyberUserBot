import time
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events


@r(outgoing=True, pattern="^.sreply (.*)$")
async def _(q):
    if q.get_reply_message():
        vaxt_ = int(q.pattern_match.group(1))
        reply_ = await q.get_reply_message()
        text_ = reply_.text

        smsg = await q.client.send_message(q.chat_id, text_)
        await q.edit("`Mesaj {vaxt} saniyə içində özünü yox edəcək.`".format(vaxt=vaxt_))

        time.sleep(vaxt_)
        await smsg.delete()

@r(outgoing=True, pattern="^.smsg (.*) ?(\w*)$")
async def _(q):
    text_ = q.pattern_match.group().split()
    vaxt_ = text_[1]
    msg_ = " "
    text_.remove(text_[0])
    text_.remove(text_[0])
    for i in text_:
        msg_+=i+" "
    smsg = await q.client.send_message(q.chat_id, msg_)
    await q.edit("`Mesaj {vaxt} saniyə içində özünü yox edəcək.`".format(vaxt=vaxt_))
    time.sleep(int(vaxt_))
    await smsg.delete()

c('mesaj').add_command(
    "sreply", "<mesaja_cavab_ver + vaxt>", "Cavab verdiyiniz mesaj qeyd etdiyiniz saniyə sonra özünü məhv edər. Nümunə: `.sreply 12`"
    ).add_command(
    "smsg", "<vaxt> <yazı>", "Yazdığınız söz qeyd etdiyiniz saniyə sonra özünü məhv edər. Nümunə: `.smsg 12 Salam`"
    ).add()
