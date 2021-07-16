import re
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
