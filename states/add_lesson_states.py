

from aiogram.dispatcher.filters.state import State, StatesGroup

# yangi dars qo'shish statelar
class Add_Lesson_State(StatesGroup):
    password = State()
    videoId = State()
    NumberOfLesson = State()
    info = State()
    youtube = State()
    telegram = State()
    category = State()
    subcategory = State()
    