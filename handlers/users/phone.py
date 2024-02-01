from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(text="Telefon narxlar")
async def bot_sozlamalar(message: types.Message):
    await message.answer(f"Sozlamalar, {message.from_user.full_name}!",reply_markup=menu)

