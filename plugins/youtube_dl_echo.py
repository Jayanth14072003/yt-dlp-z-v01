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
    youtube_dl_username = None
    youtube_dl_password = None
    file_name = None
    
    chk = await bot.send_message(
            chat_id=update.chat.id,
            text=f'<b>Processing... ⏳</b>',
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
          )
  
    if "jiocinema" in text_from_user:
        url = text_from_user
        print(url)
        if "|" in url:
            url_parts = url.split("|")
            if len(url_parts) == 2:
                url = url_parts[0]
                file_name = url_parts[1]
            elif len(url_parts) == 4:
                url = url_parts[0]
                file_name = url_parts[1]
                youtube_dl_username = url_parts[2]
                youtube_dl_password = url_parts[3]
            else:
                for entity in update.entities:
                    if entity.type == "text_link":
                        url = entity.url
                    elif entity.type == "url":
                        o = entity.offset
                        l = entity.length
                        url = url[o:o + l]
            if url is not None:
                url = url.strip()
            if file_name is not None:
                file_name = file_name.strip()
            # https://stackoverflow.com/a/761825/4723940
            if youtube_dl_username is not None:
                youtube_dl_username = youtube_dl_username.strip()
            if youtube_dl_password is not None:
                youtube_dl_password = youtube_dl_password.strip()
            logger.info(url)
            logger.info(file_name)
        else:
            for entity in update.entities:
                if entity.type == "text_link":
                    url = entity.url
                elif entity.type == "url":
                    o = entity.offset
                    l = entity.length
                    url = url[o:o + l]
        return url   
        global dlink
        dlink = url
    else:
        await bot.edit_message_text(
        text=f'<b>I can download only JioCinema links..?\nSend jiocinema links to download...!!</b>',
        chat_id=update.message.chat.id,
        message_id=update.message.message_id
        )


def GetLink():
    return GetUrl(bot, update)
