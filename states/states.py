from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):
    fronEnd = State()
    backEnd = State()
    grafikDizayn = State()
    Kompyuter= State()


class BackButtonStates(StatesGroup):
    level1 = State()
    level2 = State()
    level3 = State()

class Keraklidasturlar(StatesGroup):
    KeraklidasturLevel1 = State()
    KeraklidasturLevel2 = State()
    KeraklidasturLevel3 = State()