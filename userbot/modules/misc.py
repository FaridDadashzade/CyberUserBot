# CYBERUSERBOT - Luciferxz #


""" Cyber Misc """

from random import randint
from asyncio import sleep
from os import execl
import sys
import io
import sys
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import CYBER_VERSION
import asyncio
import os
import requests

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("misc")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.resend")
async def resend(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        event.edit(LANG['REPLY_TO_FILE'])
        return
    await event.respond(m)

@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ .random  """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            LANG['NEED_MUCH_DATA_FOR_RANDOM']
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(f"**{LANG['QUERY']}: **\n`" + items.text[8:] + f"`\n**{LANG['RESULT']}: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ .sleep """
    if " " not in time.pattern_match.group(1):
        await time.reply(LANG['SLEEP_DESC'])
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit(LANG['SLEEPING'])
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "Botu" + str(counter) + "saniyə yuxuya buraxdın.",
            )
        await sleep(counter)
        await time.edit(LANG['GOODMORNIN_YALL'])


@register(outgoing=True, pattern="^.shutdown$")
async def shutdown(event):
    """ .shutdown """
    await event.client.send_file(event.chat_id, 'https://www.winhistory.de/more/winstart/mp3/winxpshutdown.mp3', caption=LANG['GOODBYE_MFRS'], voice_note=True)
    await event.delete()

    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot söndürüldü.")
    try:
        await bot.disconnect()
    except:
        pass


@register(outgoing=True, pattern="^.restart$")
async def restart(event):
    await event.edit(LANG['RESTARTING'])
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot yenidən başladıldı.")

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)


@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ .support """
    await wannahelp.edit(LANG['SUPPORT_GROUP'])


@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    await e.edit(LANG['CREATOR'])


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(LANG['CREATOR'])


# 
@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ .repo """
    await wannasee.edit(LANG['REPO'])

@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Həll edilmiş mesaj üçün userbot loglarını yoxlayın`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Həll edilən mesaj`")
        
@register(pattern="^.instagram (.*)",outgoing=True)
async def igza(event):
    username = event.pattern_match.group(1)
    last = username.lower()
    try:
        await event.edit("`Melumatlar getirilir..`")
        os.system("pip install instaloader")
        import instaloader
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, last)
        pp = profile.get_profile_pic_url()
        ad = profile.full_name
        if not ad:
          ad = "Bu istifadəçinin ad qoymağa ehtiyyacı var."
        bio = profile.biography
        if not bio:
          bio = "Bu istifadəçinin bio qoymağa ehtiyyacı var."
        follover = profile.followers
        res = profile.is_verified
        post = profile.mediacount
        folloving = profile.followees
        url = profile.external_url
        biznes = profile.is_business_account
        gizli = profile.is_private
        aydi = profile.userid
        r = requests.get(pp) 
        with open("oyeman.jpg", "wb")as file: 
          file.write(r.content) 
        igtv = profile.igtvcount
        msg = f'''
       **Hesab məlumatları:**
         **Username:** [{last}](https://instagram.com/{last})
         **ID:** `{aydi}`
         **Ad:** `{ad}`
         **Bio:** `{bio}`
         **Followers:** `{follover}`
         **Following:** `{folloving}`
         **Post sayı:** `{post}`
         **IgTv sayı:** `{igtv}`
         **Hesab doğrulanıbmı:** `{res}`
         **Xarici bağlantı:** `{url}`
         **Gizli hesabdırmı:** `{gizli}`
         **Biznes hesabıdırmı:** `{biznes}`
            '''
        await event.delete()
        await event.client.send_file(event.chat_id,"oyeman.jpg",caption=msg)
        os.remove("oyeman.jpg")
    except:
        await event.edit("xəta")

CmdHelp('misc').add_command(
    'random', '<əşya1> <əşya2> ... <əşya3>', 'Əşya listindən təsadufi bir əşya seçər', 'random uniborg userge'
).add_command(
    'sleep', '<vaxt>', 'Bot da bir insandır, o da yorulur. Ara bir biraz yatmağına icazə ver.', 'sleep 30'
).add_command(
    'shutdown', None, 'Nostaljik bir şəkildə botunuzu söndürər.'
).add_command(
    'repo', None, 'Cyber botunun GitHub\'dakı reposuna gedən bir link.'
).add_command(
    'readme', None, 'Cybdr botunun GitHub\'dakı README.md faylına gedən bir link.'
).add_command(
    'creator', None, 'Bu botu kimin yaratdığını öyrən :)'
).add_command(
    'repeat', '<rəqəm> <mətin>', 'Bir mətini bəlli bir sayıda təkrar edər. Spam əmri ilə qarışdırmayın.'
).add_command(
    'restart', None, 'Botu yenidən başladar.'
).add_command(
    'resend', None, 'Bir medyayı yenidən göndərər.'
).add_command(
    'resend', None, 'Bir medyayı yenidən göndərər.'
).add_command(
    'raw', '<cavab>', 'Cavab verilən mesaj haqqında məlumat verər.'
).add_command(
    'instagram', None, 'Verdiyiniz Instagram hesabı haqqda məlumat verər ⌨️ İstifadəsi: .instagram "accountname"' 
).add()
