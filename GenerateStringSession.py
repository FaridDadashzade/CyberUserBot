import asyncio
import os
import sys
import time
import random

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.utils import get_display_name
from telethon.sessions import StringSession

try:
   import requests
   import bs4
except:
   print("[!] Requests tapılmadı. Yüklənir...")
   print("[!] Bs4 tapılmadı. Yüklənir...")

   if os.name == 'nt':
      os.system("python3.8 -m pip install requests")
      os.system("python3.8 -m pip install bs4")
   else:
      os.system("pip3 install requests")
      os.system("pip3 install bs4")


# Original Source https://github.com/LonamiWebs/Telethon/master/telethon_examples/interactive_telegram_client.py #
loop = asyncio.get_event_loop()

class InteractiveTelegramClient(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        print('@TheCyberUserBot String Alıcıya Xoş Gəldiniz!')
        print('[i] Telegramın Serverlərinə bağlanılır...')
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            print('[!] Bağlanarkən bir xəta baş verdi. Yenidən yoxlanılır...')
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
               user_phone = input('[?] Telefon Nömrəniz (Məsələn +994xxxxxxxxx): ')
            else:
               user_phone = telefon
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                self_user = None
            except PhoneNumberInvalidError:
                print("[!] Yanlış nömrə yazdınız nümunədəki kimi yazın. Nümunə: +994xxxxxxxxx")
                exit(1)
            except ValueError:
               print("[!] Yanlış nömrə yazdınız nümunədəki kimi yazın. Örnek: +994xxxxxxxxx")
               exit(1)

            while self_user is None:
                code = input('[?] Teleqramdan gələn 5 xanalı kodu qeyd edin: ')
                try:
                    self_user =\
                        loop.run_until_complete(self.sign_in(code=code))
                except PhoneCodeInvalidError:
                    print("[!] Kodu səhv yazdınız. Yenidən yoxlayın.")
                except SessionPasswordNeededError:
                    pw = input('[i] İki faktorlu doğrulama aşkar edildi.. '
                                 '[?] Şifrənizi yazın: ')
                    try:
                        self_user =\
                            loop.run_until_complete(self.sign_in(password=pw))
                    except PasswordHashInvalidError:
                        print("[!] 2 faktorlu şifrəni səhv yazdınız. Yenidən yoxlayın..")


if __name__ == '__main__':
   print("[i] C Y B Σ R String V3\n@TheCyberUserBot\n\n")
   print("[1] Avtomatik API ID/HASH Almaq")
   print("[2] String Almaq\n")
   
   try:
      secim = int(input("[?] Seçiminizi edin: "))
   except:
      print("[!] Xahiş edirəm bir rəqəm qeyd edin!")

   if secim == 2:
      API_ID = input('[?] API ID\'iniz [Hazır Key\'leri Kullanmak İçin Boş Bırakınız]: ')
      if API_ID == "":
         print("[i] Hazırlanır...")
         API_ID = 4
         API_HASH = "014b35b6184100b085b0d0572f9b5103"
      else:
         API_HASH = input('[?] API HASH\'iniz: ')

      client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH)
      print("[i] String Key aşağıdadır!\n\n\n" + client.session.save())
   elif secim == 1:
      numara = input("[?] Telefon Nömrəniz: ")
      try:
         rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
      except:
         print("[!] Kodu göndərmək olmadı. Telefon nömrənizi yoxlayın.")
         exit(1)
      
      sifre = input("[?] Telegram'dan gələn kodu yazın: ")
      try:
         cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
      except:
         print("[!] Böyük ehtimalla kodu səhv yazdınız. Scripti yenidən başladın.")
         exit(1)
      app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
      soup = bs4.BeautifulSoup(app, features="html.parser")

      if soup.title.string == "Create new application":
         print("[i] Proqramınız yoxdur. Yaradılır...")
         hashh = soup.find("input", {"name": "hash"}).get("value")
         AppInfo = {
            "hash": hashh,
            "app_title":"CYBERUSERBOT",
            "app_shortname": "cyber" + str(random.randint(9, 99)) + str(time.time()).replace(".", ""),
            "app_url": "",
            "app_platform": "android",
            "app_desc": ""
         }
         app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
         print(app)
         print("[i] Proqram uğurla yaradıldı!")
         print("[i] API ID/HASH alınır...")
         newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
         newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

         g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Məlumatlar gətirildi! Xahiş edirəm bunları qeyd edin.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] String almaq istəyirsən? [Almaq üçün 1 yaz]: "))
         except:
            print("[!] Xahiş edirəm rəqəm qeyd edin!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] String Key aşağıdadır!\n\n\n" + client.session.save())
         else:
            print("[i] Script dayandırılır...")
            exit(1)
      elif  soup.title.string == "App configuration":
         print("[i] Hal-hazır da Proqramənız var. API ID/HASH alınır...")
         g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Məlumatlar gətirildi! Xahiş edirəm bunları qeyd edin.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] String almaq istəyirsən? [Almaq üçün 1 yaz]: "))
         except:
            print("[!] Xahiş edirəm bir rəqəm qeyd edin!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] String Key aşağıdadır!\n\n\n" + client.session.save())
         else:
            print("[i] Script dayandırılır...")
            exit(1)
      else:
         print("[!] Bir xəta baş verdi.")
         exit(1)
   else:
      print("[!] Bilinməyən seçim.")
