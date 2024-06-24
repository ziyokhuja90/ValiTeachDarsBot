 
from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import Text
from keyboards.default import kerakliDasturlar , simpleKeyboards
from states import states
from aiogram.dispatcher import FSMContext   
from loader import bot


Apps = {
    "dizayn":{
        "photoshop":{
            "P15":"BQACAgIAAxkBAAIHLGZVf6ELSrfk42seCN71RLMOZsYIAAIKDwACTZvYS9VhJ1iA6ngbNQQ",
            "P17":"BQACAgIAAxkBAAIHNGZVgbfX1D4mFi-wZtwddLOxce8UAAIQDwACTZvYS6F4zVdGVRPvNQQ",
            "P18":"BQACAgIAAxkBAAIHLmZVgOwAAWLnEZDVDXW-t21nkpu8RgACFA8AAk2b2EtaY4GhT6-ttjUE",
            "P19":"BQACAgIAAxkBAAIHOmZVrR35nYqdRKpF6u-wAmvY41jTAAIfDwACTZvYS8G-nCU95rDPNQQ",
            "P20":"BQACAgIAAxkBAAIHMGZVgQ1_jlFPVSfN3gocovK1kClPAALMDwACTZvgS7iT3BYl6-jONQQ",
            "P21":"BQACAgIAAxkBAAIHPGZVrXOFd0rOJSMn0r06kd_YJbbgAALSDwACQ0_gS_-o4FWfAXv6NQQ",
            "P22":"BQACAgIAAxkBAAIHPmZVrZASX0EQn_94OUtgfMaLk8zSAAIOEAACbMOZSj0v6KHU7fgENQQ",
            "P23":"BQACAgIAAxkBAAIHQGZVra4RAlv0s9RvAAG_rBssYVat3gACpSIAAiFHqUioHu6OLJV2UTUE",
        },
        "Illustrator":{
            "I14":"BQACAgIAAxkBAAIHQmZVrhmny_uaYoz5XUtyv1g6LaJGAAI8EAACQ0_gS8fyp2bph_qHNQQ",
            "I15":"BQACAgIAAxkBAAIHRGZVrjTu7Mtwm3NLoMpl5Yki8yxbAAJDEAACQ0_gSz_hDdyJ6XS3NQQ",
            "I17":"BQACAgIAAxkBAAIHRmZVrmAmrRnCvUsZXrwn-iIECBfLAAJcEAACQ0_gS4_dcXeFbvWDNQQ",
            "I18":"BQACAgIAAxkBAAIHSGZVrnoZfoa4QkYOqfH5-7vCSqeFAAKPEAACQ0_gS5waCZd2KR7SNQQ",
            "I19":"BQACAgIAAxkBAAIHSmZVrp_AVGNduMeFpmJgjMybC_71AAKaEAACQ0_gS5ax2D1zxhxeNQQ",
            "I20":"BQACAgIAAxkBAAIHTGZVrsUZ0HZMh6IVNaNKb1D7GbD5AAKfEAACQ0_gS_wckZ6TtFo1NQQ",
            "I21":"BQACAgIAAxkBAAIHTmZVruDs_yhHJjVh9muUyQIEk02ZAAKjEAACQ0_gS3rqUiogKsjhNQQ",
            "I22":"BQACAgIAAxkBAAIHUGZVrvZixZuLFbcSIntFwGB0drmVAALhDwACbMOZSqMpomFlyQbWNQQ",
        },
        "Corel":{
            "MLCorel":"BQACAgIAAxkBAAIOC2ZgOtFTCHcF7tokOxFeFctCZKt2AAKTTQACI6MJSyiMrvnFTW3JNQQ",
            "Corel":"BQACAgIAAxkBAAIOVWZha-Psvu4CZDGdaCFCU4KWBFrVAAJJRQACI6MRS-eCNzf4rhRtNQQ"
        }
    },
    "dasturlash":{
        "VSCode":"BQACAgIAAxkBAAIJS2ZYNvr_kVT4RDJqWA4liErlSiNMAALdUgAC7VHBSmteWNPZq3IQNQQ",
        "Sublime":"BQACAgIAAxkBAAIJTWZYVVAzZYxbMHCp7I8NUjg21nsDAAJuVAAC7VHBStbO6uF0FROXNQQ"
    }

}



@dp.message_handler(Text(contains="Kerakli dasturlar"))
async def Keraklidasturlar(message: Message):
    await states.Keraklidasturlar.KeraklidasturLevel1.set()
    await message.answer(text="Dasturlar" , reply_markup=kerakliDasturlar.DasturlarKeyboard)


@dp.message_handler(Text(contains="Orqaga") ,state=states.Keraklidasturlar.KeraklidasturLevel1)
async def KeraklidasturlarOrqagalevel1(message: Message , state : FSMContext):
    await state.finish()
    await message.answer(text=f"{message.text}" , reply_markup=simpleKeyboards.HomeKeyboards)

@dp.message_handler(Text("Dasturlash dasturlar") , state=states.Keraklidasturlar.KeraklidasturLevel1)
async def KearklidasturlarDasturlash(message : Message , state : FSMContext):
    await states.Keraklidasturlar.KeraklidasturLevel2.set()
    await message.answer(text="Kerakli dasturlar",reply_markup=kerakliDasturlar.KeraklidasturlarDasrulash)



@dp.message_handler(Text("Grafik dizayn dasturlar") , state=states.Keraklidasturlar.KeraklidasturLevel1)
async def KearklidasturlarDasturlash(message : Message , state : FSMContext):
    await states.Keraklidasturlar.KeraklidasturLevel2.set()
    await message.answer(text="Kerakli dasturlar", reply_markup=kerakliDasturlar.KeraklidasturlarGrafikdizaynKeyboard)

@dp.message_handler(Text(contains="Orqaga"), state=states.Keraklidasturlar.KeraklidasturLevel2)
async def KeraklidasturlarOrqagaLevel2(message: Message , state : FSMContext):
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel1.set()
    await message.answer(text=f"{message.text}" , reply_markup=kerakliDasturlar.DasturlarKeyboard)


@dp.message_handler(Text("Adobe Photoshop") , state=states.Keraklidasturlar.KeraklidasturLevel2)
async def KearklidasturlarDasturlash(message : Message , state : FSMContext):
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel3.set()
    await message.answer(text="Adobe Photoshop dasturlar", reply_markup=kerakliDasturlar.KeraklidasturlarPhotoshopKeyboard)

@dp.message_handler(Text("Adobe Illustrator") , state=states.Keraklidasturlar.KeraklidasturLevel2)
async def KearklidasturlarIllustrator(message : Message , state : FSMContext):
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel3.set()
    await message.answer(text="Adobe Illustrator dasturlar", reply_markup=kerakliDasturlar.KeraklidasturlarIllustratorKeyboard)

@dp.message_handler(Text("Coreldraw") , state=states.Keraklidasturlar.KeraklidasturLevel2)
async def KearklidasturlarCorelDraw(message : Message , state : FSMContext):
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel3.set()
    await message.answer(text="CorelDraw dasturlar", reply_markup=kerakliDasturlar.KeraklidasturlarCorelDrawKeyboard)



@dp.message_handler(Text(contains="Orqaga"), state=states.Keraklidasturlar.KeraklidasturLevel3)
async def KeraklidasturlarOrqagaLevel2(message: Message , state : FSMContext):
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel2.set()
    await message.answer(text=f"{message.text}" , reply_markup=kerakliDasturlar.KeraklidasturlarGrafikdizaynKeyboard)


@dp.message_handler(Text(contains="Adobe Photoshop 20") , state=states.Keraklidasturlar.KeraklidasturLevel3)
async def KearklidasturlarDasturlash(message : Message , state : FSMContext):

    for app in Apps["dizayn"]["photoshop"]:
        if message.text[-2:] == str(app[-2:]):
            await bot.send_document(chat_id=message.from_user.id ,document=Apps["dizayn"]["photoshop"][app] )
        else:
            print(message.text[-2:])
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel3.set()
    # await mesasge.answer(text="dasturlar", reply_markup=kerakliDasturlar.KeraklidasturlarPhotoshopKeyboard)

@dp.message_handler(Text(contains="Adobe Illustrator CC 20") , state=states.Keraklidasturlar.KeraklidasturLevel3)
async def KearklidasturlarDasturlash(message : Message , state : FSMContext):


    for app in Apps["dizayn"]["Illustrator"]:
        if message.text[-2:] == str(app[-2:]):
            await bot.send_document(chat_id=message.from_user.id ,document=Apps["dizayn"]["Illustrator"][app] )
        else:
            print(message.text[-2:])
    await state.finish()
    await states.Keraklidasturlar.KeraklidasturLevel3.set() 




@dp.message_handler(Text("Visual studio code"), state=states.Keraklidasturlar.KeraklidasturLevel2)
async def Visualstudiocode(message: Message ):
    await bot.send_document(chat_id=message.from_user.id , document=Apps["dasturlash"]["VSCode"])


@dp.message_handler(Text("Sublime text"),state=states.Keraklidasturlar.KeraklidasturLevel2)
async def Visualstudiocode(message: Message ):
    await bot.send_document(chat_id=message.from_user.id , document=Apps["dasturlash"]["Sublime"])


@dp.message_handler(Text("ML_CorelDraw 2022"),state=states.Keraklidasturlar.KeraklidasturLevel3)
async def MLCorel(message: Message ):
    await bot.send_document(chat_id=message.from_user.id , document=Apps["dizayn"]["Corel"]["MLCorel"])


@dp.message_handler(Text("CorelDraw 2022"),state=states.Keraklidasturlar.KeraklidasturLevel3)
async def Corel(message: Message ):
    await bot.send_document(chat_id=message.from_user.id , document=Apps["dizayn"]["Corel"]["Corel"])
