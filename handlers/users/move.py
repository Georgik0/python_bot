from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.choice_button import choice
from start import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="Какой-то текст номер 1", reply_markup=choice)
