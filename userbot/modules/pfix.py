# Copyright (C) 2021 FaridDadashzade.
#
# CyberUserBot - FaridDadashzade
# All rights reserved.

import re
import os
from telethon.tl.types import DocumentAttributeFilename, InputMessagesFilterDocument
import importlib
import time
import traceback

from userbot import bot, tgbot, PATTERNS
from userbot.events import register
from userbot.main import extractCommands
