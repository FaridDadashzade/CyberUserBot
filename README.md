----

<p align="center"><a href="https://t.me/TheCyberUserBot"><img src="https://telegra.ph/file/dd1a82e8454f7fe3c04d8.jpg" width="400"></a></p> 
<h1 align="center"><b>C Y B Σ R USΣRBOT 🇦🇿</b></h1>
</div>
<p align="center">
    C Y B Σ R UserBot, Telegram istifadəsini asanlaşdıran bir proyektdir. Müəllif hüquqları MIT Licence ilə qorunur.
    
</p>

----

## Qurulum
### Avtomatik Qurulum

**Android:** Termuxu açın ve bu kodu yapışdırın: `bash <(curl -L https://bit.ly/2SuGkcA)`

**iOS:** iSH açın ve bu kodu yapışdırın: `apk update && apk add bash && apk add curl && curl -L -o cyber_installer.sh https://git.io/JYKsg && chmod +x cyber_installer.sh && bash cyber_installer.sh`

**Windows** `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://git.io/JOHQ2')`

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/FaridDadashzade/CyberUserBot)

### Çətin Yol
```python
git clone https://github.com/FaridDadashzade/CyberUserBot.git
cd CyberUserBot
pip install -r requirements.txt
# Config.env yaradın və düzəldin. #
python3 main.py
```

## String Session

[![Run on Repl.it](https://repl.it/badge/github/FaridDadashzade/Cyber)](https://repl.it/@FaridDadashzade/Cyber)

## Plugin Düzəltmək
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunların yazılması vacibdir.

@register(outgoing=True, pattern="^.yoxlama")
async def deneme(event):
    await event.edit('Yoxlamadan sonraki edit!')

Help = CmdHelp('yoxlama') # Bilgi əlavə etmək isdədiyimizi deyirik
Help.add_command('deneme', # Bura əmr qismini yazırsınız
    None, # Əmr parametri varsa yazın yoxsa None yazın
    'Bu yoxlama Edir!', # Əmr açıqlaması hansiki plugin yüklənəndən sonra Açığlama qismində yazılan
    'deneme' # Misal üçün göstərə biləcəyiniz istifadə tipi.
    )
Help.add_info('@Luciferxz tərəfindən hazırlanmışdır.') # Məlumat əlavə edirik (burda kim tərəfindən hazırlanıb və s. bildirə bilərsiniz.
# Ya da Xəbərdarlıq --> Help.add_warning('Xəbərdarlıq!')
Help.add() # Və Əlavə Edək.
```

## Qeyd
```
    UserBot ilə əlaqəli; Telegram hesabınız bağlana bilər.
    Bu bir açıq qaynaqlı proyektdir, CYBER Sahibləri və Adminləri olaraq heç bir cavabdehlik daşımırıq.
    CYBER quraraq bu cavabdehlikləri qəbul etmiş sayılırsınız.
```

