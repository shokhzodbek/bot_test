from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu = ReplyKeyboardMarkup(keyboard=[
    [
     KeyboardButton(text="🚅 Click Premium"),
     KeyboardButton(text="🚌 Kartalarim"),
     ],
],resize_keyboard=True)

lang = ReplyKeyboardMarkup(keyboard=[
    [
     KeyboardButton(text="Uz"),
     KeyboardButton(text="Ru"),
     ],
],resize_keyboard=True)

