from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton

from loader import db
from keyboards.default import simpleKeyboards


# async def SubCategoryKeyboard(category):
    
#     # print(db.select_all_SubCategorys())
#     Subcategorys = db.select_Subcategory(category=category)
#     # print(Subcategorys)
#     SubcategoryKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

#     Subcategory_buttons = []
#     SubcategorySet = set(Subcategory[1] for Subcategory in Subcategorys)

#     # Manually arrange buttons into rows of two
#     row = []
#     for subcategory in SubcategorySet:
#         row.append(subcategory)
#         if len(row) == 2:
#             Subcategory_buttons.append(row)
#             row = []

#     # If there are any remaining buttons, add them to the last row
#     if row:
#         Subcategory_buttons.append(row)

#     # Add buttons to the keyboard
#     for row in Subcategory_buttons:
#         SubcategoryKeyboard.row(*row)

#     new_keyboard = SubcategoryKeyboard
#     new_keyboard.add(simpleKeyboards.back_button , simpleKeyboards.main_menu_button)
    
#     return new_keyboard
