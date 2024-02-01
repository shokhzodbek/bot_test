from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.akula import f
from filters import IsPrivate
from loader import dp
import logging

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    logging.info(message.chat.title)
    await message.answer(f"Assalomu alaykum, {message.chat.title} !",reply_markup=f)
