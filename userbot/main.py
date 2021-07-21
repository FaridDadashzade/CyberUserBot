# Copyright (C) 2021 Farid Dadashzade
#
# Telegram: @faridxz

import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, CYBER_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

ALIVE_STR = [
    "`C Y B Ξ R sahibinin əmirlərinə hazırdır...`",
    "✨ `C Y B Ξ R` **{mention}**-in `əmirlərinə hazırdır...`",
    "⛈️ **{mention}** `əlimdən gələnin ən yaxşısını etməyə hazıram...`",
]

KICKME_STR = [
    "Bye bye mən gedirəm! 🦦",
    "Qrupu tərk edirəm! 😒",
    "Qrupdan çıxıram..\nBir daha dönməmək şərti ilə!",
    "Qrupdan ayrılıram... 🦦",
]

DIZCILIK_STR = [
    "Stikeri oğurlayıram...",
    "Bu stikeri çox bəyəndimmm...",
    "Bu stikeri öz paketimə əlavə edirəm...",
    "Bunu oğurlamalıyamm...",
    "Hey bu əla stikerdir!\nElə indi oğurlayıram..",
    "Stikerini oğurladım\nhahaha.",
    "Hey bura bax. (☉｡☉)!→\nMən bunu oğurlayarkən...",
    "Bu stikeri paketimə əlavə edirəm...",
    "Stiker paketə əlavə edilir...",
    "Stikeri öz paketimə əlavə edirəm... ",
]

AFKSTR = [
    "İndi vacib işim var, daha sonra mesaj atsan olmaz? Onsuzda yenə gələcəm.",
    "Hörmətli istifadəçi zəng etdiyiniz şəxs hazırda telefona cavab verə bilmir.",
    "Bir neçə dəqiqə içində gələcəm lakin gəlməsəm...\nbiraz daha gözlə.",
    "İndi burada deyiləm..\nYəqin ki, başqa bir yerdəyəm..",
    "Sahibim hal-hazırda AFK-dır!",
    "Bəzən həyatdakı ən yaxşı şeylər gözləməyə dəyər…\nGələcəm.",
    "Gələcəm,\namma əgər gəlməsəm,\ndaha sonra gələrəm.",
    "Hal-hazırda sahibim burada deyil.\nXahiş edirəm biraz sonra əlaqə saxlayın.",
    "Çox heyif ki sahibim burada deyil..",
    "İndi burada deyiləm..\nTezliklə qayıdacağam..",
    "Sahibim burada deyil..\nqayıdanda sizinlə əlaqə saxlayacaqdır.",
    "Gələcəm,\namma əgər gəlməsəm,\ndaha sonra gələrəm.",
    "Bir neçə dəqiqə içində gələcəm lakin gəlməsəm..\nbiraz daha gözlə.",
    "Hey, sahibim hal-hazırda burada deyil..\nqayıtdığında sizinlə əlaqə saxlayacaqdır.",
]

UNAPPROVED_MSG = ("`Salam,` {mention} `!\nBu bir avtomatik mesajdır. Narahat olma.\n\n`"
                  "`Sahibim sənə PM yazma icazəsi verməyib. `"
                  "`Zəhmət olmasa sahibimin aktiv olmasını gözləyin, o bəzən PM yazmağa icazə verər.\n\n`"
                  "`Bildiyim qədəri ilə o beynini itirib insanlara PM icazəsi vermir.`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nXƏTA: Yazılan telefon nömrəsi yanlışdır' \
             '\n  Tips: Ölkə kodunu istifadə edərək yenidən yaz' \
             '\n       Telefon nömrənizi kontrol edin.'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

       
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

           
            Cyberpy = re.search('\"\"\"CYBERPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Cyberpy == None:
                Cyberpy = Cyberpy.group(0)
                for Satir in Cyberpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin xaricdən yüklənib, hər hansı bir açıqlama qeyd olunmayıb.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    cyberbl = requests.get('https://raw.githubusercontent.com/FaridDadashzade/deploy/main/cyberbl.json').json()
    if idim in cyberbl:
        bot.send_message("me", f"`C Y B Ξ R adminləri tərəfindən botdan istifadə haqqınız alındı.`")
        LOGS.error("C Y B Ξ R adminləri tərəfindən botunuz dayandırıldı.")
        bot.disconnect()

    
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    
    GALERI = {}

    
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_STR))}", "afk": f"`{str(choice(AFKSTR))}`", "kickme": f"{str(choice(KICKME_STR))}", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, Banlandı!`", "mute": "{mention}`, səssizə alındı!`", "approve": "{mention}`, artıq mənə mesaj göndərə bilərsən!`", "disapprove": "{mention}`, artıq mənə mesaj göndərə bilməzsən!`", "block": "{mention}`, səni əngəllədim!`"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("Pluginlər yüklənir...")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu plugin onsuzda yüklüdür " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Yükləmədə problem! Plugin xətalıdır.\n\nXəta: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Xahiş edirəm pluginlerin qalıcı olması üçün PLUGIN_CHANNEL_ID'i ayarlayın.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Botunuz işləyir! Hər-hansısa bir söhbətə .alive yazaraq test edin."
          " Köməyə ehtiyacınız olarsa, dəstək qrupumuza gəlin t.me/TheCyberSupport")
LOGS.info(f"Version: C Y B Ξ R {CYBER_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
