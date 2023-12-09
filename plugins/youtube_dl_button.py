# -*- coding: utf-8 -*-
#By KA18 the @legend580 💛❤️

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import json
import math
import os
import shutil
import time
from datetime import datetime
from jlink import ptitle, pmpd, pkey
from plugins.config import Config
from plugins.translation import Translation
# from plugins.custom_thumbnail import *
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram.types import InputMediaPhoto
from plugins.stuff import progress_for_pyrogram, humanbytes, random_char
# from plugins.database.database import db
from PIL import Image
# from functions.ran_text import random_char

async def main_j_bot(bot, update):
    youtube_dl_url = pmpd
    random1 = random_char(5)
    custom_vfile_name = "video" + ".mp4"
    custom_dvfile_name = "videos" + ".mp4"
    custom_afile_name = "audio" + ".m4a"
    custom_dafile_name = "audios" + ".m4a"
    youtube_dl_username = None
    youtube_dl_password = None
    if "|" in youtube_dl_url:
        url_parts = youtube_dl_url.split("|")
        if len(url_parts) == 2:
            youtube_dl_url = url_parts[0]
            custom_file_name = url_parts[1]
        elif len(url_parts) == 4:
            youtube_dl_url = url_parts[0]
            custom_file_name = url_parts[1]
            youtube_dl_username = url_parts[2]
            youtube_dl_password = url_parts[3]
        else:
            for entity in update.message.reply_to_message.entities:
                if entity.type == "text_link":
                    youtube_dl_url = entity.url
                elif entity.type == "url":
                    o = entity.offset
                    l = entity.length
                    youtube_dl_url = youtube_dl_url[o:o + l]
        if youtube_dl_url is not None:
            youtube_dl_url = youtube_dl_url.strip()
        if custom_file_name is not None:
            custom_file_name = custom_file_name.strip()
        # https://stackoverflow.com/a/761825/4723940
        if youtube_dl_username is not None:
            youtube_dl_username = youtube_dl_username.strip()
        if youtube_dl_password is not None:
            youtube_dl_password = youtube_dl_password.strip()
        logger.info(youtube_dl_url)
        logger.info(custom_file_name)
    else:
        for entity in update.message.reply_to_message.entities:
            if entity.type == "text_link":
                youtube_dl_url = entity.url
            elif entity.type == "url":
                o = entity.offset
                l = entity.length
                youtube_dl_url = youtube_dl_url[o:o + l]
    await bot.edit_message_text(
        text=Translation.DOWNLOAD_START,
        chat_id=update.message.chat.id,
        message_id=update.message.message_id
    )
    description = Translation.CUSTOM_CAPTION_UL_FILE
    if description is None:
          description = ptitle
          #description = response_json["fulltitle"][0:1021]
        # escape Markdown and special characters
    tmp_directory_for_each_user = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + f'{random1}'
    if not os.path.isdir(tmp_directory_for_each_user):
        os.makedirs(tmp_directory_for_each_user)
    download_V_directory = tmp_directory_for_each_user + "/" + custom_vfile_name
    download_DV_directory = tmp_directory_for_each_user + "/" + custom_dvfile_name
    download_A_directory = tmp_directory_for_each_user + "/" + custom_afile_name
    download_DA_directory = tmp_directory_for_each_user + "/" + custom_dafile_name
    download_FV_directory = tmp_directory_for_each_user + "/" + ptitle + ".mkv"
    command_to_exec = []
    if youtube_dl_url is not None:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
          )
        #downloading video
        command_to_exec = [
            "yt-dlp",
            "-f", "video=600000"
            "--max-filesize", str(Config.TG_MAX_FILE_SIZE),
            youtube_dl_url,
            "--allow-unplayable",
            "-o", download_V_directory
        ]
        if Config.HTTP_PROXY != "":
            command_to_exec.append("--proxy")
            command_to_exec.append(Config.HTTP_PROXY)
        if youtube_dl_username is not None:
            command_to_exec.append("--username")
            command_to_exec.append(youtube_dl_username)
        if youtube_dl_password is not None:
            command_to_exec.append("--password")
            command_to_exec.append(youtube_dl_password)
        command_to_exec.append("--no-warnings")
        # command_to_exec.append("--quiet")
        logger.info(command_to_exec)
        start = datetime.now()
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
        logger.info(e_response)
        logger.info(t_response)
        ad_string_to_replace = "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."
        if e_response and ad_string_to_replace in e_response:
            error_message = e_response.replace(ad_string_to_replace, "")
            await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=error_message
            )
            return False

        # downloading audio
        command_to_exec = [
            "yt-dlp",
            "-f", "bestaudio"
            youtube_dl_url,
            "--allow-unplayable",
            "-o", download_A_directory
        ]

        await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=f"Downloading audio..!!"
            )

        command_to_exec.append("--no-warnings")
        # command_to_exec.append("--quiet")
        logger.info(command_to_exec)
        # start = datetime.now()
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()

        # Decrypting video
        command_to_exec = [
            'mp4decrypt',
            '--key',pkey,
            download_V_directory,download_DV_directory
        ]
        await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=f"Decrypting video..!!"
            )
        logger.info(command_to_exec)
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()

        # Decrypting audio
        command_to_exec = [
            'mp4decrypt',
            '--key',pkey,
            download_A_directory,download_DA_directory
        ]
        await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=f"Decrypting audio..!!"
            )
        logger.info(command_to_exec)
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()

        # Merging video and audio
        command_to_exec = [
            'ffmpeg',
            '-i', download_DV_directory,'-i', download_DA_directory,'-vcodec' ,'copy' ,'-acodec' ,'copy',download_FV_directory
        ]
        await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=f"Merging video and audio..!!"
            )
        logger.info(command_to_exec)
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
      
        end_one = datetime.now()
        time_taken_for_download = (end_one -start).seconds
        file_size = Config.TG_MAX_FILE_SIZE + 1
        try:
            file_size = os.stat(download_FV_directory).st_size
        except FileNotFoundError as exc:
            download_FV_directory = os.path.splitext(download_FV_directory)[0] + "." + "mkv"
            # https://stackoverflow.com/a/678242/4723940
            file_size = os.stat(download_FV_directory).st_size
        if file_size > Config.TG_MAX_FILE_SIZE:
            await bot.edit_message_text(
                chat_id=update.message.chat.id,
                text=Translation.RCHD_TG_API_LIMIT.format(time_taken_for_download, humanbytes(file_size)),
                message_id=update.message.message_id
            )
        else:
            is_w_f = False
            '''images = await generate_screen_shots(
                download_directory,
                tmp_directory_for_each_user,
                is_w_f,
                Config.DEF_WATER_MARK_FILE,
                300,
                9
            )
            logger.info(images)'''
            await bot.edit_message_text(
                text=f"Download completed.",
                chat_id=update.message.chat.id,
                message_id=update.message.message_id
            )

            # ref: message from @Sources_codes
            start_time = time.time()
            if os.path.exists(download_FV_directory):
                try:
                    thumbnail = await Gthumb(bot, update)
                    await bot.send_document(
                        chat_id=update.message.chat.id,
                        document=download_FV_directory,
                        thumb=thumbnail,
                        caption=description,
                        reply_to_message_id=update.message.reply_to_message.message_id,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            "Uploading Document..!",
                            update.message,
                            start_time
                        )
                    )
                except:
                     width, height, duration = await Mdata01(download_directory)
                     thumb_image_path = await Gthumb(bot, update, duration, download_directory)
                     await bot.send_video(
                        chat_id=update.message.chat.id,
                        video=download_FV_directory,
                        caption=description,
                        duration=duration,
                        width=width,
                        height=height,
                        supports_streaming=True,
                        thumb=thumb_image_path,
                        reply_to_message_id=update.message.reply_to_message.message_id,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            "Uploading Video",
                            update.message,
                            start_time
                        )
                    )
            
            else:
                logger.info("Did this happen? :\\")
                await bot.send_message(
                text=f"Downloaded file not found..!",
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                disable_web_page_preview=True
                )
              
            end_two = datetime.now()
            time_taken_for_upload = (end_two - end_one).seconds
            try:
                shutil.rmtree(tmp_directory_for_each_user)
                os.remove(thumbnail)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS.format(time_taken_for_download, time_taken_for_upload),
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                disable_web_page_preview=True
            )
    # Delete the contenet(video and audio stuff)
    # os.remove(tmp_directory_for_each_user)
    else:
        # command_to_exec = ["youtube-dl", "-f", youtube_dl_format, "--hls-prefer-ffmpeg", "--recode-video", "mp4", "-k", youtube_dl_url, "-o", download_directory]
        await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=f"There is problem with your link please send valid link..!!"
            )

    if t_response:
        logger.info(t_response)
        try:
            os.remove(save_ytdl_json_path)
        except FileNotFoundError as exc:
            pass
        
