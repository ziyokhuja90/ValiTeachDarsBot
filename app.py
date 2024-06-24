from aiogram import executor

from loader import dp , db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    try:
        # db.delete_table_lesson()
        # db.create_table_lesson()
        # db.delete_Subcategory_lesson()
        print("Bot ishga tushdi")
        # db.create_table_category()
        # db.delete_Category_lesson()
        # db.create_table_subcategory()
        # db.create_table_users()
    except Exception as err:
        print(err)
        # print("sssssss")
        


    
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
