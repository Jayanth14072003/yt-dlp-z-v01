#By KA18 the @legend580 💛❤️

import os
# from functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
# from plugins.dl_button import ddl_call_back
# from plugins.youtube_dl_button import youtube_dl_call_back
# from plugins.settings.settings import OpenSettings
from plugins.translation import Translation
from pyrogram import Client, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from plugins.database.database import db
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif "close" in update.data:
        await update.message.delete(True)

    # elif "|" in update.data:
    #     await youtube_dl_call_back(bot, update)
    # elif "=" in update.data:
    #     await ddl_call_back(bot, update)

    else:
        await update.message.delete()
