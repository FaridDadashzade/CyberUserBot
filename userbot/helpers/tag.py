# CYBERUSERBOT
#

import re, os
from random import choice
import logging

from telethon import events
from telethon.extensions.markdown import DEFAULT_URL_RE
from telethon.tl import types
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.types import (
    MessageEntityBold,
    MessageEntityCode,
    MessageEntityItalic,
    MessageEntityPre,
    MessageEntityTextUrl,
    MessageEntityUnderline,
)

#------------------ CYBERUSERBOT -------------------#


PARSED_ENTITIES = (
    MessageEntityBold,
    MessageEntityItalic,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextUrl,
    MessageEntityUnderline,
)


#------------------ CYBERUSERBOT -------------------#

MATCHERS = [
    (DEFAULT_URL_RE, parse_url_match),
    (get_tag_parser("**", MessageEntityBold)),
    (get_tag_parser("__", MessageEntityItalic)),
    (get_tag_parser("```", partial(MessageEntityPre, language=""))),
    (get_tag_parser("`", MessageEntityCode)),
    (get_tag_parser("--", MessageEntityUnderline)),
    (re.compile(r"\+\+(.+?)\+\+"), parse_aesthetics),
    (re.compile(r"([^/\w]|^)(/?(r/\w+))"), parse_subreddit),
    (re.compile(r"(?<!\w)(~{2})(?!~~)(.+?)(?<!~)\1(?!\w)"), parse_strikethrough),
]


def get_tag_parser(tag, entity):
    def tag_parser(m):
        return m.group(1), entity(offset=m.start(), length=len(m.group(1)))

    tag = re.escape(tag)
    return re.compile(tag + r"(.+?)" + tag, re.DOTALL), tag_parser


async def tag(event):
    newstr = event.text
    if event.entities:
        newstr = nameexp.sub(r'<a href="tg://user?id=\2">\3</a>', newstr, 0)
        for match in usernexp.finditer(newstr):
            user = match.group(1)
            text = match.group(2)
            name, entities = await event.client._parse_message_text(text, "md")
            rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
            if entities:
                for e in entities:
                    tag = None
                    if isinstance(e, types.MessageEntityBold):
                        tag = "<b>{}</b>"
                    elif isinstance(e, types.MessageEntityItalic):
                        tag = "<i>{}</i>"
                    elif isinstance(e, types.MessageEntityCode):
                        tag = "<code>{}</code>"
                    elif isinstance(e, types.MessageEntityStrike):
                        tag = "<s>{}</s>"
                    elif isinstance(e, types.MessageEntityPre):
                        tag = "<pre>{}</pre>"
                    elif isinstance(e, types.MessageEntityUnderline):
                        tag = "<u>{}</u>"
                    if tag:
                        rep = tag.format(rep)
            newstr = re.sub(re.escape(match.group(0)), rep, newstr)
    if newstr != event.text:
        await event.edit(newstr, parse_mode="html")
