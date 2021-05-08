# CYBERUSERBOT - Luciferxz #


import os
from requests import post
from userbot import bot, OCR_SPACE_API_KEY, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("ocr")

# ████████████████████████████████ #

async def ocr_space_file(filename,
                         overlay=False,
                         api_key=OCR_SPACE_API_KEY,
                         language='tur'):
    """ OCR.space API yerli fayl istəyər
        Python3.5 və üzəri üçün - 2.7 üzərində test edilmədi.
    :param filename: fayl yolu və adı.
    :param overlay: Cavabınızda OCR.space yerləşimi vacibdir mi?
                    Həmişəlik olaraq Xeyr.
    :param api_key: OCR.space API key.
                    həmişəlik olaraq 'salamdünya'.
    :param language: OCR'də işlədiləcək dil kodu.
                    Mövcus dil kodlarının listi buradan tapa bilər https://ocr.space/OCRAPI
                    Həmişəlik olaraq 'tr'.
    :return: Nəticələr JSON formatında gəlir.
    """

    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
    }
    with open(filename, 'rb') as f:
        r = post(
            'https://api.ocr.space/parse/image',
            files={filename: f},
            data=payload,
        )
    return r.json()


@register(pattern=r".ocr (.*)", outgoing=True)
async def ocr(event):
    await event.edit(LANG['READING'])
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await bot.download_media(
        await event.get_reply_message(), TEMP_DOWNLOAD_DIRECTORY)
    test_file = await ocr_space_file(filename=downloaded_file_name,
                                     language=lang_code)
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
    except BaseException:
        await event.edit(LANG['CANT_READ'])
    else:
        await event.edit(f"`{LANG['READ']}`\n\n{ParsedText}"
                         )
    os.remove(downloaded_file_name)

CmdHelp('ocr').add_command(
    'ocr', '<dil>', 'Mətin aydınlatmaq üçün bir fotoya vəya stikerə cavab verin.'
).add_info(
    'Dil kodlarını [buradan](https://ocr.space/ocrapi) götürün.'
).add()
