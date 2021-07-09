# Copyright (C) 2021 FaridDadashzade
#
# Cyber UserBot - faridxz

from userbot import CMD_HELP, ASYNC_POOL, tgbot, SUDO_ID, SPOTIFY_DC, G_DRIVE_CLIENT_ID, lastfm, YOUTUBE_API_KEY, OPEN_WEATHER_MAP_APPID, AUTO_PP, REM_BG_API_KEY, OCR_SPACE_API_KEY, PM_AUTO_BAN, BOTLOG_CHATID, CYBER_VERSION
from userbot.events import register
from telethon import version
from platform import python_version
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("durum")

# ████████████████████████████████ #

def durum(s):
    if s == None:
        return "❌"
    else:
        if s == False:
            return "❌"
        else:
            return "✅"

@register(outgoing=True, pattern="^.durum|^.status")
async def durums(event):

    await event.edit(f"""
**Python {LANG['VERSION']}:** `{python_version()}`
**TeleThon {LANG['VERSION']}:** `{version.__version__}` 
**C Y B Ξ R {LANG['VERSION']}:** `{CYBER_VERSION}`

**{LANG['PLUGIN_COUNT']}:** `{len(CMD_HELP)}`

**Inline Bot:** `{durum(tgbot)}`
**Spotify:** `{durum(SPOTIFY_DC)}`
**Sudo:** `{durum(SUDO_ID)}`
**GDrive:** `{durum(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{durum(lastfm)}`
**YouTube ApiKey:** `{durum(YOUTUBE_API_KEY)}`
**OpenWeather:** `{durum(OPEN_WEATHER_MAP_APPID)}`
**AutoPP:** `{durum(AUTO_PP)}`
**RemoveBG:** `{durum(REM_BG_API_KEY)}`
**OcrSpace:** `{durum(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{durum(PM_AUTO_BAN)}`
**BotLog:** `{durum(BOTLOG_CHATID)}`
**Plugin:** `{LANG['PERMAMENT']}`

**{LANG['OK']} ✅**
    """)

CmdHelp('status').add_command(
    'status', None, 'Əlavə olunan apiləri və versiyonları göstərir.'
).add()
