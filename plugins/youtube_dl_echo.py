#By KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import requests, urllib.parse, filetype, os, time, shutil, tldextract, asyncio, json, math
from PIL import Image
from plugins.config import Config
import time
from plugins.translation import Translation
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters
from pyrogram import Client
from plugins.stuff import progress_for_pyrogram, humanbytes, TimeFormatter, random_char
# from plugins.youtube_dl_button import main_j_bot
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Thumbnail

# jiocinema link extractor
from pathlib import Path
import subprocess
import jwt
import requests
import re
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import asyncio

#for  keys
import base64, requests, sys, xmltodict, json
from WKSKEYS.pywidevin.L3.cdm import deviceconfig
from base64 import b64encode
from WKSKEYS.pywidevin.L3.getPSSH import get_pssh
from WKSKEYS.pywidevin.L3.decrypt.wvdecryptcustom import WvDecrypt
import time
import re

@Client.on_message(filters.private & filters.regex(pattern=".*http.*"))
async def GetUrl(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    # await add_user_to_database(bot, update)
    await bot.send_chat_action(
       chat_id=update.chat.id,
       action="typing"
    )
    logger.info(update.from_user)
    text_from_user = update.text
    chk = await bot.send_message(
            chat_id=update.chat.id,
            text=f'<b>Processing... ⏳</b>',
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
          )
    if "jiocinema" in text_from_user:
        url = text_from_user
        print(url)
        logger.info(url)
        global dlink
        dlink = url
        # main_j_bot(bot, update)
        await chk.dlete()
        return url   
        
    else:
        await bot.edit_message_text(
        text=f'<b>I can download only JioCinema links..?\nSend jiocinema links to download...!!</b>',
        chat_id=update.message.chat.id,
        message_id=update.message.message_id
        )

def GetLink():
    a=GetUrl(bot, update)
    return a
