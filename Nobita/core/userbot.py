# Powered By NOBITA_XD IF You Fresh Any Problem To Contact The  Owner

import sys

from pyrogram import Client

from Nobita import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"🌷 ɢᴇᴛᴛɪɴɢs ᴀssɪsᴛᴀɴᴛ ɪɴғᴏ 🔍...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AAPLI_YARRI")
                await self.one.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ ᴀs {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ  1 sᴛᴀʀᴛᴇᴅ 🌺.\n\n✅ ɴᴀᴍᴇ :**{self.one.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.one.username}\n🌷 ɪᴅ : {self.one.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 1 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ  💥 "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("AAPLI_YARRI")
                await self.two.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 2 sᴛᴀʀᴛᴇᴅ.\n\n✅ ɴᴀᴍᴇ :{self.two.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.two.username}\n🌷 ɪᴅ : {self.two.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 2 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ  2 sᴛᴀʀᴛᴇᴅ  ᴀs {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("AAPLI_YARRI")
                await self.three.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"🌷sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 3 sᴛᴀʀᴛᴇᴅ .\n\n✅ ɴᴀᴍᴇ :{self.three.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.three.username}\n🌷 ɪᴅ : {self.three.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 3 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 3 sᴛᴀʀᴛᴇᴅ ᴀs {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("AAPLI_YARRI")
                await self.four.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 4 sᴛᴀʀᴛᴇᴅ  ᴀs .\n\n✅ ɴᴀᴍᴇ :{self.four.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.four.username}\n🌷 ɪᴅ : {self.four.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 4 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ  4 sᴛᴀʀᴛᴇᴅ {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("AAPLI_YARRI")
                await self.five.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 5 sᴛᴀʀᴛᴇᴅ  ᴀs .\n\n✅ ɴᴀᴍᴇ :{self.five.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ:** @{self.five.username}\n🌷 ɪᴅ : {self.five.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 5 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ  🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ 💥"

                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 5 sᴛᴀʀᴛᴇᴅ {self.five.name}"
            )
