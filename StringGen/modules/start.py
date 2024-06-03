import asyncio
from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    jishubotz_sticker = await message.reply_sticker("CAACAgUAAxkBAAECEEBlLA-nYcsWmsNWgE8-xqIkriCWAgACJwEAAsiUZBTiPWKAkUSmmh4M")
    
    # 2 seconds ka wait
    await asyncio.sleep(2)
    
    # Sticker delete karna
    await jishubotz_sticker.delete()
    
    # Photo ke saath caption set karna
    photo_url = 'https://graph.org/file/b17ef9fea2b440246068a.jpg'
   
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nAɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.\n\n🌿 ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/LPRPDV'>❚█═𝗠𝗿. 𝗟𝗣𝗥𝗣𝗗𝗩═█❚</a>",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
