from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from aiogram.dispatcher import FSMContext   
from states.states import States , BackButtonStates

from loader import dp , db , bot 

from keyboards.default import kerakliDasturlar
from keyboards.default import simpleKeyboards
# from keyboards.default.categorykeyboards import categoryKeyboard
# from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.LessonKeyboards import LessonKeyboards
from keyboards.default.simpleKeyboards import StartLesson ,  dasturlashKeyboard , HomeKeyboards


@dp.message_handler(Text(contains="bog'lanish") , state="*")
async def MainMenuHandler(message: types.Message , state: FSMContext):
    # await state.finish()
    await message.answer("Biz bilan bog'lanish uchun ushbu qo'ng'iroqlarga qo'ng'iroq qilishingiz mumkin \n+998945515701 \n+998910585717")

@dp.message_handler(Text(contains="Bot haqida") , state="*")
async def MainMenuHandler(message: types.Message , state: FSMContext):
    # await state.finish()
    await message.answer("Bu bot orqali siz IT sohasi bo'yicha tekin darsliklarni ko'rib mustaqil o'rganishingiz mumkin")



@dp.message_handler(Text(contains="Menyu") , state="*")
async def MainMenuHandler(message: types.Message , state: FSMContext):
    await state.finish()
    await message.answer("Bosh bo'lim" , reply_markup=HomeKeyboards)

@dp.message_handler(Text("Bepul Darslar"))
async def startLesson(message: types.Message):
    print(message.reply_markup)
    await message.answer("Quyidagi bo'limlardan birini tanlang.", reply_markup=HomeKeyboards)


@dp.message_handler(Text('Grafik dizayn') , state='*')
async def grafikdizaynHandler(message: types.Message):

    await States.grafikDizayn.set()

    await message.answer("Kursni tanlang" , reply_markup=simpleKeyboards.grafikdizayn)

IsDizaynlesson = bool()

@dp.message_handler(state=States.grafikDizayn)
async def GrakifdizaynlessonHandler(message : types.Message , state: FSMContext):
    global IsDizaynlesson
    
    if message.text == "🔙 Orqaga" and IsDizaynlesson == True :
        IsDizaynlesson = False
        print(IsDizaynlesson)
        await message.answer("Orqaga", reply_markup=simpleKeyboards.grafikdizayn)

    elif message.text == "🔙 Orqaga" :
        IsDizaynlesson = False
        await state.finish()
        # await BackButtonStates.level1.set()
        await message.answer("Orqaga", reply_markup=HomeKeyboards)
    else:
        lessons = await db.select_lesson(category="Grafik Dizayn"  , subcategory=message.text)

        if lessons != []:
            global subcategory
            IsDizaynlesson = True
            subcategory = message.text
            keyboard = await LessonKeyboards(category="Grafik Dizayn" , subcategory=message.text)
            print(keyboard)
            await message.answer("Dars sonini tanlang" , reply_markup=keyboard)
        else:
            IsDizaynlesson = True
            text = f""
            try:
                if len(message.text) != 7:
                    lesson = await db.select_lessonLessonNumber(lesson_number=message.text[0] , category_name="Grafik Dizayn" , subcategory_name=subcategory)
                else:
                    lesson = await db.select_lessonLessonNumber(lesson_number=message.text[:2] , category_name="Grafik Dizayn" , subcategory_name=subcategory)
                text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
                text += f"Youtube — {lesson[0][5]} \n\n"
                text += f"Telegram — {lesson[0][4]} \n\n"

                await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text , )
            # await state.finish()
            except:
                pass






@dp.message_handler(Text("Dasturlash") , state="*")
async def startLesson(message: types.Message):

    await BackButtonStates.level1.set()
    await message.answer("Kursni tanlang", reply_markup=simpleKeyboards.dasturlashKeyboard)

@dp.message_handler(Text(contains="Orqaga"), state=BackButtonStates.level1)
async def dasturlashBackButtonHandler(message : types.Message ,  state : FSMContext):
    await state.finish()
    await message.answer(message.text , reply_markup=HomeKeyboards)


@dp.message_handler(Text("Front-end") ,state="*")
async def SubCategory(message : types.Message , state : FSMContext):
    await States.fronEnd.set()
    keyboard = simpleKeyboards.FrontendKeyboard
    

    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)


@dp.message_handler(Text("Back-end") , state="*")
async def SubCategory(message : types.Message , state : FSMContext):
    await States.backEnd.set()
    keyboard = simpleKeyboards.BackendKeyboard

    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)

Islesson = bool()

@dp.message_handler(state=States.fronEnd)
async def lessonKeyboards(message: types.Message, state: FSMContext):
    global keyboardLessons
    global Islesson
    if message.text == "🔙 Orqaga" and Islesson == True :
        Islesson = False
        print(Islesson)
        keyboardFront = simpleKeyboards.FrontendKeyboard
        await message.answer("Orqaga", reply_markup=keyboardFront)

    elif message.text == "🔙 Orqaga" :
        Islesson = False
        await state.finish()
        await BackButtonStates.level1.set()
        await message.answer("Orqaga", reply_markup=dasturlashKeyboard)

    else:
        lessons =  db.select_lesson(category_name="Front-end"  , subcategory_name=message.text)
        print(f"darslar  === {lessons}")
        if lessons != []:
            global subcategory
            Islesson = True
            subcategory = message.text
            keyboard = await LessonKeyboards(category="Front-end" , subcategory=message.text)

            await message.answer("Dars sonini tanlang" , reply_markup=keyboard)
        else:
            Islesson = True
            text = f""
            try:
                if len(message.text) != 7:
                    lesson =  db.select_lesson(lesson_number=message.text[0] , category_name="Front-end" , subcategory_name=subcategory)
                else:
                    lesson =  db.select_lesson(lesson_number=message.text[:2] , category_name="Front-end" , subcategory_name=subcategory)
                print("dars" , lesson)
                text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
                text += f"Youtube — {lesson[0][5]} \n\n"
                text += f"Telegram — {lesson[0][4]} \n\n"

                await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text  )
            except:
                pass


IslessonBackend  = bool()
@dp.message_handler(state=States.backEnd)
async def lessonKeyboards(message : types.Message , state : FSMContext):
    global keyboardLessons
    global IslessonBackend
    if message.text == "🔙 Orqaga" and IslessonBackend == True :
        IslessonBackend = False
        print(Islesson)
        keyboardBackend = simpleKeyboards.BackendKeyboard
        await message.answer("Orqaga", reply_markup=keyboardBackend)

    elif message.text == "🔙 Orqaga" :
        IslessonBackend = False
        await state.finish()
        await BackButtonStates.level1.set()
        await message.answer("Orqaga", reply_markup=dasturlashKeyboard)

    else:
        lessons =  db.select_lesson(category_name="Back-end"  , subcategory_name=message.text)
        print(f"darslar  === {lessons}")
        if lessons != []:
            global subcategory
            Islesson = True
            subcategory = message.text
            keyboard = await LessonKeyboards(category="Back-end" , subcategory=message.text)

            await message.answer("Dars sonini tanlang" , reply_markup=keyboard)
        else:
            Islesson = True
            text = f""
            try:
                if len(message.text) != 7:
                    lesson =  db.select_lesson(lesson_number=message.text[0] , category_name="Back-end" , subcategory_name=subcategory)
                else:
                    lesson =  db.select_lesson(lesson_number=message.text[:2] , category_name="Back-end" , subcategory_name=subcategory)
                
                print("dars" , lesson)
                text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
                text += f"Youtube — {lesson[0][5]} \n\n"
                text += f"Telegram — {lesson[0][4]} \n\n"

                await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text  )
            except:
                pass


@dp.message_handler(Text("Kompyuter savodxonligi"))
async def KompyuterSavodxonligi(message : types.Message):
    keyboard = await LessonKeyboards("Kompyuter savodxonligi","Kompyuter savodxonligi")
    await States.Kompyuter.set()
    
    await message.answer(message.text , reply_markup=keyboard)






@dp.message_handler(state=States.Kompyuter)
async def KompyuterSavodxonligiLesson(message : types.Message , state: FSMContext):
    
    if message.text == "🔙 Orqaga":
        await message.answer("Orqaga", reply_markup=simpleKeyboards.HomeKeyboards)
        await state.finish
    else:
        text = f""
        try:
            if len(message.text) != 7:
                lesson =  db.select_lesson(lesson_number=message.text[0] , category_name="Kompyuter savodxonligi" , subcategory_name="Kompyuter savodxonligi")
            else:
                lesson =  db.select_lesson(lesson_number=message.text[:2] , category_name="Kompyuter savodxonligi" , subcategory_name="Kompyuter savodxonligi")
            
            text += f"Kompyuter savodxonligi Darslari | {message.text} | {lesson[0][3]} \n\n"
            text += f"Youtube — {lesson[0][5]} \n\n"
            text += f"Telegram — {lesson[0][4]} \n\n"

            await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text , )

        except:
            pass