from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from filters import IsGroup,AdminFilter
import logging

@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"Assalomu alaykum grupada yaxshi bola bul, {message.chat.title}! ")
    
@dp.message_handler(IsGroup(), AdminFilter(),text="salom",)
@dp.message_handler(IsGroup(),text="hi")
async def hi(message: types.Message):
    logging.info(message)
    await message.answer(f"Va alaykum assalom, yaxshimisan! {message.from_user.full_name} ")