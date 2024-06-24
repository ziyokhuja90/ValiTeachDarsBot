
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from uuid import uuid4
from loader import dp , db
from aiogram.dispatcher import FSMContext   

from keyboards.default.simpleKeyboards import StartLesson


uuid = uuid4()
@dp.message_handler(CommandStart() , state="*")
async def bot_start(message: types.Message ,state : FSMContext):
    await state.finish()

    await message.answer(f"Salom, {message.from_user.full_name}!" , reply_markup=StartLesson)