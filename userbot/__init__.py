# Copyright (C) 2021 Farid Dadashzade
# 
# CyberUserBot - faridxz
#

""" UserBot hazırlanışı. """

import os
from re import compile
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, custom
from telethon.sessions import StringSession
from telethon.events import callbackquery, InlineQuery, NewMessage
from math import ceil

load_dotenv("config.env")

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

ASYNC_POOL = []

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - @TheCyberUserBot - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - @TheCyberUserBot - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("Ən az Python 3.6 versiyasına sahib olmanız lazımdır."
              "Birdən çox özəllik buna bağlıdır. Bot bağlanır.")
    quit(1)


CONFIG_CHECK = os.environ.get(
    "___________XAIS_______BU_____SETIRI_____SILIN__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Xahiş edirik ilk hashtag'de qeyd edilən sətiri config.env faylından silin"
    )
    quit(1)

# Bot'un dili
LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()

if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
    LOGS.info("Bilinməyən bir dil yazdınız. Buna görə DEFAULT istifadə edilir.")
    LANGUAGE = "DEFAULT"
    
# CYBER VERSION
CYBER_VERSION = "v1.7"

# SUDO VERSION
SUDO_VERSION = "v1.0"

# API KEY və API HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

try:
    SUDO_ID = set(int(x) for x in os.environ.get("SUDO_ID", "").split())
except ValueError:
    raise Exception("SUDO_ID qeyd etməmisiniz!")

SILINEN_PLUGIN = {}
# StringSession
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Kanal / Grup ID günlüyə qeyd etmə
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# JARVIS
AUTO_UPDATE =  sb(os.environ.get("AUTO_UPDATE", "True"))

# UserBot log özəlliyi
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Hey! Bu botdur. qormxa ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# ALIVE_NAME
ALIVE_NAME = str(os.environ.get("ALIVE_NAME")) or None

# ALIVE
ALIVE_NAME = os.environ.get("ALIVE_NAME") or None

# Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/74bcd15eee31dc2631b81.mp4"

# Zip modulu üçün
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY") or "./zips"

# Alive mesajı üçün ".set var DEFAULT_NAME Adınız"
DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)

# Güncəlləmə üçün
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)

# Guncelleme ucun
UPSTREAM_REPO_URL = "https://github.com/FaridDadashzade/CyberUserBot.git"

# CONSOLE LOGGER VERBOSE
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///cyber.db")

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# AUTO PP
AUTO_PP = os.environ.get("AUTO_PP", None)

# Warn modulu
WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE = os.environ.get("WARN_MODE", "gmute")

if not WARN_MODE in ["gmute", "gban"]:
    WARN_MODE = "gmute"

# Qalareya
GALERI_SURE = int(os.environ.get("GALERI_SURE", 60))

# Chrome
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

PLUGINID = os.environ.get("PLUGIN_CHANNEL_ID", None)
# Plugin üçün
if not PLUGINID:
    PLUGIN_CHANNEL_ID = "me"
else:
    PLUGIN_CHANNEL_ID = int(PLUGINID)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Anti Spambot
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Saat & Tarix - Ölkə və Saat Dilimi
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# CLEAN WELCOME
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm modulu
BIO_PREFIX = os.environ.get("BIO_PREFIX", "@TheCyberUserBot | ")
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Modulu
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Botun işləməsi üçün
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Genius
GENIUS = os.environ.get("GENIUS", None)
CMD_HELP = {}
CMD_HELP_BOT = {}
PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 4))

SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)

PAKET_ISMI = os.environ.get("PAKET_ISMI", "@TheCyberUserBot Paketi")

# Avtomatik qatılma
OTOMATIK_KATILMA = sb(os.environ.get("OTOMATIK_KATILMA", "True"))

# Whitelist and Patterns
PATTERNS = os.environ.get("PATTERNS", ".;!,")
WHITELIST = get('https://raw.githubusercontent.com/FaridDadashzade/deploy/main/whitelist.json').json()
SUPPORT = [1527722982, 979515849]

# CloudMail.ru və MEGA.nz ayarlama
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' dəyişgəni
if STRING_SESSION:
    # pylint: deaktiv=sehv ad
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: deaktiv=sehv ad
    bot = TelegramClient("userbot", API_KEY, API_HASH)

JARVIS = 1852686126
JARVISUSERNAME = 'fjarvisbot'

if os.path.exists("learning-data-root.check"):
    os.remove("learning-data-root.check")
else:
    LOGS.info("Braincheck dosyası yoxdur, gətirilir...")

URL = 'https://raw.githubusercontent.com/quiec/databasescape/master/learning-data-root.check'
with open('learning-data-root.check', 'wb') as load:
    load.write(get(URL).content)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "Özəl xəta günlüyünün çalışması üçün BOTLOG_CHATID ayarlayın.")
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Özəl xəta günlüyünün çalışması üçün BOTLOG_CHATID ayarlayın.")
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Hesabınızın BOTLOG_CHATID qrupuna mesaj göndərmə yetkisi yoxdur. "
            "Qrup ID'sini doğru yazıb yazmadığınızı kontrol edin.")
        quit(1)
        
if not BOT_TOKEN == None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None

def butonlastir(sayfa, moduller):
    Satir = 5
    Kolon = 2
    
    moduller = sorted([modul for modul in moduller if not modul.startswith("_")])
    pairs = list(map(list, zip(moduller[::2], moduller[1::2])))
    if len(moduller) % 2 == 1:
        pairs.append([moduller[-1]])
    max_pages = ceil(len(pairs) / Satir)
    pairs = [pairs[i:i + Satir] for i in range(0, len(pairs), Satir)]
    butonlar = []
    for pairs in pairs[sayfa]:
        butonlar.append([
            custom.Button.inline("✅ " + pair, data=f"bilgi[{sayfa}]({pair})") for pair in pairs
        ])

    butonlar.append([custom.Button.inline("⬅️ Geri", data=f"sayfa({(max_pages - 1) if sayfa == 0 else (sayfa - 1)})"), custom.Button.inline("İrəli ➡️", data=f"sayfa({0 if sayfa == (max_pages - 1) else sayfa + 1})")])
    return [max_pages, butonlar]

with bot:
    if OTOMATIK_KATILMA:
        try:
            bot(JoinChannelRequest("@TheCyberUserBot"))
            bot(JoinChannelRequest("@TheCyberSupport"))
        except:
            pass

    moduller = CMD_HELP
    me = bot.get_me()
    uid = me.id

    try:
        @tgbot.on(NewMessage(pattern='/start'))
        async def start_bot_handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'`Salam mən `@TheCyberUserBot`! Mən sahibimə (`@{me.username}`) kömək üçün varam, yəni sənə kömək edə bilmərəm. Amma sən də özünə C Y B Σ R qura bilərsən. Kanala bax` @TheCyberUserBot')
            else:
                await event.reply(f'`Salam mən `@TheCyberUserBot`! Mən sahibimə (`@{me.username}`) kömək üçün varam, yəni sənə kömək edə bilmərəm. Amma sən də özünə C Y B Σ R qura bilərsən. Kanala bax` @TheCyberUserBot`')

        @tgbot.on(InlineQuery)  
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query == "@TheCyberUserBot":
                rev_text = query[::-1]
                veriler = (butonlastir(0, sorted(CMD_HELP)))
                result = await builder.article(
                    f"Xahiş edirəm sadəcə .help əmrini istifadə edin.",
                    text=f"**C Y B Σ R USERBOT** [C Y B Σ R](https://t.me/TheCyberUserBot) __işləyir...__\n\n**Yüklü olan modul sayı:** `{len(CMD_HELP)}`\n**Səhifə:** 1/{veriler[0]}",
                    buttons=veriler[1],
                    link_preview=False
                )
            elif query.startswith("http"):
                parca = query.split(" ")
                result = builder.article(
                    "Fayl yükləndi",
                    text=f"**Fayl uğurla {parca[2]} saytına yükləndi!**\n\nYükləmə zamanı: {parca[1][:3]} saniyə\n[‏‏‎ ‎]({parca[0]})",
                    buttons=[
                        [custom.Button.url('URL', parca[0])]
                    ],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "@TheCyberUserBot",
                    text="""@TheCyberUserBot-u işlətməyi yoxlayın!
Hesabınızı bot'a çevirə bilərsiniz və bunları istifadə edə bilərsiniz.""",
                    buttons=[
                        [custom.Button.url("Kanala Qatıl", "https://t.me/TheCyberUserBot"), custom.Button.url(
                            "Qrupa Qatıl", "https://t.me/TheCyberSupport")],
                        [custom.Button.url(
                            "GitHub", "https://github.com/FaridDadashzade/CyberUserBot")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)

        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"sayfa\((.+?)\)")))
        async def sayfa(event):
            if not event.query.user_id == uid: 
                return await event.answer("❌ Hey! Mənim mesajlarımı dəyişməyə çalışma! Özünə bir @TheCyberUserBot qur.", cache_time=0, alert=True)
            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            veriler = butonlastir(sayfa, CMD_HELP)
            await event.edit(
                f"**C Y B Σ R USERBOT** [C Y B Σ R](https://t.me/TheCyberUserBot) __işləyir...__\n\n**Yüklü olan modul sayı:** `{len(CMD_HELP)}`\n**Sayfa:** {sayfa + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"bilgi\[(\d*)\]\((.*)\)")))
        async def bilgi(event):
            if not event.query.user_id == uid: 
                return await event.answer("❌ Hey! Mənim mesajlarımı dəyişməyə çalışma! Özünə bir @TheCyberUserBot qur.", cache_time=0, alert=True)

            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            komut = event.data_match.group(2).decode("UTF-8")
            try:
                butonlar = [custom.Button.inline("⚜ " + cmd[0], data=f"komut[{komut}[{sayfa}]]({cmd[0]})") for cmd in CMD_HELP_BOT[komut]['commands'].items()]
            except KeyError:
                return await event.answer("❌ Bu modula açıqlama yazılmayıb.", cache_time=0, alert=True)

            butonlar = [butonlar[i:i + 2] for i in range(0, len(butonlar), 2)]
            butonlar.append([custom.Button.inline("⬅️ Geri", data=f"sayfa({sayfa})")])
            await event.edit(
                f"**📗 Fayl:** `{komut}`\n**🔢 Əmr sayı:** `{len(CMD_HELP_BOT[komut]['commands'])}`",
                buttons=butonlar,
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))
        async def komut(event):
            if not event.query.user_id == uid: 
                return await event.answer("❌ Hey! Mənim mesajlarımı dəyişməyə çalışma! Özünə bir @TheCyberUserBot qur.", cache_time=0, alert=True)

            cmd = event.data_match.group(1).decode("UTF-8")
            sayfa = int(event.data_match.group(2).decode("UTF-8"))
            komut = event.data_match.group(3).decode("UTF-8")

            result = f"**✅ Fayl:** `{cmd}`\n"
            if CMD_HELP_BOT[cmd]['info']['info'] == '':
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                    result += f"**⚠️ Diqqət:** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                else:
                    result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
            else:
                result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⚠️ Uyarı:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
                result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

            command = CMD_HELP_BOT[cmd]['commands'][komut]
            if command['params'] is None:
                result += f"**🛠 Əmr:** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 Əmr:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n"
                result += f"**⌨️ Nümunə:** `{PATTERNS[:1]}{command['example']}`\n\n"

            await event.edit(
                result,
                buttons=[custom.Button.inline("⬅️ Geri", data=f"bilgi[{sayfa}]({cmd})")],
                link_preview=False
            )
    except Exception as e:
        print(e)
        LOGS.info(
            "Botunuzda inline dəstəyi deaktivdir. "
            "Aktivləşdirmək üçün bir bot token qeyd edin və botunuzda inline modunu aktivləşdirin. "
            "Əgər bunun xaricində bir xəts olduğunu düşünürsünüzsə, bizə yazın t.me/TheCyberSupport."
        )

    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID dəyişgəni keçərli bir varlıq deyil. "
            "Ortam dəyişgənlərinizi / config.env faylınızı kontrol edin."
        )
        quit(1)


# Dəyişgənlər
SON_GORULME = 0
COUNT_MSG = 0
USERS = {}
MYID = uid
BRAIN_CHECKER = []
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
ISAFK = False
AFKREASON = None
ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
    [
    " ̍", " ̎", " ̄", " ̅", " ̿", " ̑", " ̆", " ̐", " ͒", " ͗",
    " ͑", " ̇", " ̈", " ̊", " ͂", " ̓", " ̈́", " ͊", " ͋", " ͌",
    " ̃", " ̂", " ̌", " ͐", " ́", " ̋", " ̏", " ̽", " ̉", " ͣ",
    " ͤ", " ͥ", " ͦ", " ͧ", " ͨ", " ͩ", " ͪ", " ͫ", " ͬ", " ͭ",
    " ͮ", " ͯ", " ̾", " ͛", " ͆", " ̚"
],
    [
    " ̕",
    " ̛",
    " ̀",
    " ́",
    " ͘",
    " ̡",
    " ̢",
    " ̧",
    " ̨",
    " ̴",
    " ̵",
    " ̶",
    " ͜",
    " ͝",
    " ͞",
    " ͟",
    " ͠",
    " ͢",
    " ̸",
    " ̷",
    " ͡",
]]
