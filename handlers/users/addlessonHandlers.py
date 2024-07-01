from loader import dp , db , bot
from aiogram.types import Message

from aiogram import types

from aiogram.dispatcher import FSMContext   

from states.add_lesson_states import Add_Lesson_State

from uuid import uuid4

from keyboards.default.categorykeyboards import categoryKeyboard    
# from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.simpleKeyboards import StartLesson




# @dp.message_handler(commands=["addLesson"] , is_admin=True)
# async def AddLesson(message : Message , state : FSMContext):

#     await Add_Lesson_State.videoId.set()
#     await message.answer("Assalomu alayekum yangi dars videosini tashlang")

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def AddLessonNumberOfLesson(message:Message ,state : FSMContext):
    video_file_id = message.video.file_id

    await bot.send_message(chat_id=message.from_user.id , text=f"Video qabul qilindi \nVideo Id: {video_file_id}")
    await state.finish()

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def Dasturlar(message: Message ):
    await message.answer(message.document.file_id)
