import random 
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMoringstar
from LuciferMoringstar_Robot.database.users_chats_db import db

@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton("🔗 Movie Time", url=f"https://t.me/+4kz4z9zCyLdjZjI1")
             ],[
             InlineKeyboardButton("ℹ️ Help", callback_data="help"),
             InlineKeyboardButton("😎 About", callback_data="about") 
             ],[
             InlineKeyboardButton("🎭 Who Am I", callback_data="who")
             ]]
        else:
            buttons = [[
             InlineKeyboardButton("🔗 Movie Time", url=f"https://t.me/+4kz4z9zCyLdjZjI1")
             ],[
             InlineKeyboardButton("ℹ️ Help", callback_data="bot_owner"),
             InlineKeyboardButton("😎 About", callback_data="about") 
             ],[
             InlineKeyboardButton("🎭 Who Am I", callback_data="who")
             ]]
             reply_markup = InlineKeyboardMarkup(buttons)
             await message.reply_chat_action("typing")
             m=await message.reply_sticker("CAACAgUAAxkBAAEO6RtiO7D4w8Paf-xsd4NCdvg8efiU1wACFQEAAsiUZBRmRDCipxVsEyME") 
             await asyncio.sleep(2)
             await m.delete()
             await message.reply_chat_action("typing")
             await message.reply_photo(
                 photo=random.choice(PICS),
                 caption=LuciferMoringstar.START_MSG.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
                 reply_markup=reply_markup,
                 parse_mode='html'
             )
             await message.reply_chat_action("Typing")
             m=await message.reply_sticker("CAACAgUAAxkBAAEQ8XRiO8iXcdMUHwiie4V7IrblsmAAAQkAApwAA8iUZBRzjwAB89rFhfweBA") 
             await asyncio.sleep(20)
             await m.delete()
             return
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/dc07517edd588aad50b36.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("🔔 Movie Time Updates 🔔", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=random.choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
     InlineKeyboardButton("🏠 Home", callback_data="start"),
     InlineKeyboardButton("About 😎", callback_data="about")
     ]]
    await message.reply_photo(
        photo = random.choice(BOT_PICS),
        caption=LuciferMoringstar.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
     InlineKeyboardButton("🏠 Home", callback_data="start"),
     InlineKeyboardButton("Close 🗑️", callback_data="close")
     ],[
     InlineKeyboardButton("🎭 Who Am I", callback_data="who")
     ]]
    await message.reply_photo(
        photo=random.choice(BOT_PICS),
        caption=LuciferMoringstar.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
