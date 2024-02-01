# from aiogram import types
# from aiogram import Bot
# from loader import dp
# import logging
# from data import config

# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     logging.info(message)
#     await bot.send_message(-1002102362257, message.text)
#     await message.answer(message.text)
