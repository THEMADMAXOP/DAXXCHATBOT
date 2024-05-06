from pyrogram import filters, Client
from pyrogram.types import Message

from nexichat import OWNER, nexichat
from nexichat.database.chats import get_served_chats
from nexichat.database.users import get_served_users


@nexichat.on_message(filters.command("cstats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )
