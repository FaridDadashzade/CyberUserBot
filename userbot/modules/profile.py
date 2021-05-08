# CYBERUSERBOT - Luciferxz #


""" Profile """

import os
from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from userbot import bot, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ====================== CONSTANT ===============================
# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("profile")

# ████████████████████████████████ #

INVALID_MEDIA = LANG['INVALID_MEDIA']
PP_CHANGED = LANG['PP_CHANGED']
PP_TOO_SMOL = LANG['PP_TOO_SMOL']
PP_ERROR = LANG['PP_ERROR']

BIO_SUCCESS = LANG['BIO_SUCCESS']

NAME_OK = LANG['NAME_OK']
USERNAME_SUCCESS = LANG['USERNAME_SUCCESS']
USERNAME_TAKEN = LANG['USERNAME_TAKEN']
# ===============================================================


@register(outgoing=True, pattern="^.reserved$")
async def mine(event):
    """ .reserved  """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


@register(outgoing=True, pattern="^.name")
async def update_name(name):
    """ .name  """
    newname = name.text[6:]
    if " " not in newname:
        firstname = newname
        lastname = ""
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]

    await name.client(
        UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await name.edit(NAME_OK)


@register(outgoing=True, pattern="^.setpfp$")
async def set_profilepic(propic):
    """ .profilepic """
    replymsg = await propic.get_reply_message()
    photo = None
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await propic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await propic.client.download_file(replymsg.media.document)
        else:
            await propic.edit(INVALID_MEDIA)

    if photo:
        try:
            await propic.client(
                UploadProfilePhotoRequest(await
                                          propic.client.upload_file(photo)))
            os.remove(photo)
            await propic.edit(PP_CHANGED)
        except PhotoCropSizeSmallError:
            await propic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await propic.edit(PP_ERROR)
        except PhotoExtInvalidError:
            await propic.edit(INVALID_MEDIA)


@register(outgoing=True, pattern="^.setbio (.*)")
async def set_biograph(setbio):
    """ .setbio """
    newbio = setbio.pattern_match.group(1)
    await setbio.client(UpdateProfileRequest(about=newbio))
    await setbio.edit(BIO_SUCCESS)


@register(outgoing=True, pattern="^.username (.*)")
async def update_username(username):
    """ .username  """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)


@register(outgoing=True, pattern="^.count$")
async def count(event):
    """ .count  """
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("`Xaiş edirəm gözləyin..`")
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)

    result += f"`{LANG['USERS']}:`\t**{u}**\n"
    result += f"`{LANG['GROUPS']}:`\t**{g}**\n"
    result += f"`{LANG['SUPERGROUPS']}:`\t**{c}**\n"
    result += f"`{LANG['CHANNELS']}:`\t**{bc}**\n"
    result += f"`{LANG['BOTS']}:`\t**{b}**"

    await event.edit(result)


@register(outgoing=True, pattern=r"^.delpfp")
async def remove_profilepic(delpfp):
    """ .delpfp """
    group = delpfp.text[8:]
    if group == 'all':
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id,
                             offset=0,
                             max_id=0,
                             limit=lim))
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(id=sep.id,
                       access_hash=sep.access_hash,
                       file_reference=sep.file_reference))
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(
        LANG['DELPFP'] % len(input_photos))

CmdHelp('profile').add_command(
    'username', '<yeni istifadəçi adı>', 'Telegram\'dakı istifadəçi adınızı dəyişdirir.'
).add_command(
    'name', '<ad> or .name <ad> <soyad>', 'Telegram\'dakı adınızı dəyişdirir. (Ad və soyad ilk boşluğa dayanaraq birləşdirilir.)'
).add_command(
    'setpfp', None, 'Bir fotonu Telegram\'da profil foto etmək üçün .setpfp əmriylə cavab verin.'
).add_command(
    'setbio', '<yeni biyoqrafi>', 'Telegram\'dakı biyoqrafinizi bu əmri işlədərək dəyişdirin.'
).add_command(
    'delpfp', '<rəqəm/all>', 'Telegram profil fotosunu silər.'
).add_command(
    'reserved', None, 'Rezerve etdiyiniz istifadəçi adlarını göstərər.'
).add_command(
    'count', None, 'Qruplarınızı, söhbətlərinizi, aktiv botları vs. sayar.'
).add()
