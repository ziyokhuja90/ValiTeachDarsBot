from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton
from loader import db 
from keyboards.default import simpleKeyboards

# async def LessonKeyboards(category, subcategory):
#     lessons = await db.select_lesson(category=category, subcategory=subcategory)

#     LessonKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     row = []
#     for lesson in lessons:
#         row.append(f"{lesson['lesson_number']}-dars")
#         if len(row) == 2:  # Adjust 2 to the desired row width
#             LessonKeyboard.row(*row)
#             row = []
#     if row:  # Add the last row if it's not empty
#         LessonKeyboard.row(*row)

#     LessonKeyboard.add(simpleKeyboards.back_button, simpleKeyboards.main_menu_button)
    
#     return LessonKeyboard
    # lesson_buttons = []



    # Subcategory_buttons = []
    # SubcategorySet = set(Subcategory[1] for Subcategory in Subcategorys)

    # # Manually arrange buttons into rows of two
    # row = []
    # for subcategory in SubcategorySet:
    #     row.append(subcategory)
    #     if len(row) == 2:
    #         Subcategory_buttons.append(row)
    #         row = []

    # # If there are any remaining buttons, add them to the last row
    # if row:
    #     Subcategory_buttons.append(row)

    # # Add buttons to the keyboard
    # for row in Subcategory_buttons:
    #     SubcategoryKeyboard.row(*row)

async def LessonKeyboards(category, subcategory):
    lessons = db.select_lesson(category_name=category, subcategory_name=subcategory)
    # Extract lesson numbers and create a list in the format "number-dars"
    print("dars" , lessons)
    lesson_list = [f"{lesson[-1]}-dars" for lesson in lessons]

    # Sort lessons numerically by extracting the integer part from the string
    lesson_list.sort(key=lambda x: int(x.split('-')[0]))

    LessonKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    row = []
    for lesson in lesson_list:
        row.append(lesson)
        if len(row) == 2:  # Adjust 2 to the desired row width
            LessonKeyboard.row(*row)
            row = []
    if row:  # Add the last row if it's not empty
        LessonKeyboard.row(*row)

    # Add custom buttons
    LessonKeyboard.add(KeyboardButton("🔙 Orqaga"), KeyboardButton("🔝 Asosiy Menyu"))

    return LessonKeyboard





# dars:[(1, 'test', 'test', 'test', 'test', 'test', 'Front-end', 'HTML', '1')]