#
# Copyright (C) 2022 by NOBITA_XD 
# NOBITA_XD 
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Nobita import config
from Nobita.config import BANNED_USERS
from Nobita import LOGGER, app, userbot
from Nobita.core.call import Nobita
from plugins import ALL_MODULES
from Nobita.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("sʜɪᴢᴜᴋᴀ_ɴᴏʙɪᴍᴜsɪᴄ").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("sʜɪᴢᴜᴋᴀ_ɴᴏʙɪᴍᴜsɪᴄ").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("plugins." + all_module)
    LOGGER("plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Nobita.start()
    try:
        await Nobita.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("sʜɪᴢᴜᴋᴀ_ɴᴏʙɪᴍᴜsɪᴄ").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Nobita.decorators()
    LOGGER("sʜɪᴢᴜᴋᴀ_ɴᴏʙɪᴍᴜsɪᴄ").info("sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ᴍᴜsɪᴄ Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("sHIZUKA_NOBIMUSIC").info("Stopping sHIZUKA_NOBI Music Bot! GoodBye")
