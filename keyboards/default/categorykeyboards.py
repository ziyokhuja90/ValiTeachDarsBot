from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton

from loader import db

async def categoryKeyboard():
    categorys = await db.select_all_Categorys()
    # for category in categorys:
    #     categoryKeyboard = ReplyKeyboardMarkup(
    #         keyboard=[
    #             [KeyboardButton(category[1])],
    #         ],
    #         resize_keyboard=True
    #     )
    #     print(category)

    # categoryKeyboard = ReplyKeyboardMarkup(row_width=2 ,resize_keyboard=True)

    # categorySet = set()
    # for category in categorys:
    #     categorySet.add(category[1])

    # for i in categorySet:
    #     categoryKeyboard.add(i)

    # print(categoryKeyboard)


    categoryKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    category_buttons = []
    categorySet = set(category[1] for category in categorys)

    # Manually arrange buttons into rows of two
    row = []
    for category in categorySet:
        row.append(category)
        if len(row) == 2:
            category_buttons.append(row)
            row = []

    # If there are any remaining buttons, add them to the last row
    if row:
        category_buttons.append(row)

    # Add buttons to the keyboard
    for row in category_buttons:
        categoryKeyboard.row(*row)

    return categoryKeyboard