# Copyright (C) 2021 FaridDadashzade.
#
# CyberUserBot - @faridxz

""" CYBERUSERBOT """

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from userbot import bot, BOTLOG_CHATID, CYBER_VERSION, LOGSPAMMER, PATTERNS, JARVIS, MYID


def register(**args):
    """ Yeni bir etkinlik qeyd edin. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    insecure = args.get("insecure", False)
    jarvis = args.get('jarvis', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']
    
    if "insecure" in args:
        del args["insecure"]  

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
        
        
    if 'jarvis' in args:
        del args['jarvis']
        args['incoming'] = True
        args["from_users"] = JARVIS
        

    def decorator(func):
        async def wrapper(check):
            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                await check.respond("`Bunun bir qrup oldu??unu d??????nm??r??m!`")
                return

            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    text = "**C Y B ?? R X??TA B??LD??R??????**\n"
                    link = "[C Y B ?? R D??st??k Qrupuna](https://t.me/TheCyberSupport)"
                    if len(eventtext)<10:
                        text += f"\n**??? ??mr:** {eventtext}\n"
                    text += "\n??????? ??st??s??niz bunu biz?? bildir?? bil??rsiniz."
                    text += f" Sad??c?? bu mesaj?? {link} g??nd??rin.\n"
                    text += "X??ta v?? tarix xaricind?? he?? bir ??ey qeyd edilmir.\n"

                    ftext = "========== XEBERDARLIQ =========="
                    ftext += "\nBu fayl sad??c?? bura y??kl??nib,"
                    ftext += "\nSad??c?? x??ta v?? tarixi qeyd edirik,"
                    ftext += "\nGizliliyiniz bizim ??????n ??n??mlidir,"
                    ftext += "\nBurada h??r hans?? bir gizli m??lumat olarsa"
                    ftext += "\nBu x??ta bildiri??i olmaz, he?? k??s sizin m??lumatlar??n??z?? o??urlaya bilm??z.\n"
                    ftext += "--------USERBOT X??TA LOG--------\n"
                    ftext += "\nTarix: " + date
                    ftext += "\nQrup ID: " + str(check.chat_id)
                    ftext += "\nG??nd??r??n adam??n ID: " + str(check.sender_id)
                    ftext += "\n\n??mr:\n"
                    ftext += str(check.text)
                    ftext += "\n\nX??ta m??tni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\nDaha ??trafl??:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------USERBOT XETA LOGU SON--------"
                    ftext += "\n\n================================\n"
                    ftext += f"====== ?????? Version : {CYBER_VERSION} ======\n"
                    ftext += "================================"

                    command = "git log --pretty=format:\"%an: %s\" -5"

                    ftext += "\n\n\nSon 5 d??yi??iklik:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("cyber.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        try:
                            await check.edit("`Ba??????lay??n,\n ?????? X??ta g??nl??kl??ri UserBot g??nl??k qrupunda saxlan??l??r.`")
                        except:
                            pass
                    await check.client.send_file(send_to,
                                                 "cyber.log",
                                                 caption=text)

                    remove("cyber.log")
            else:
                pass
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator
