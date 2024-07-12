from aiogram.fsm.state import StatesGroup, State


class UserStatesGroup(StatesGroup):
    name = State()
    #surname = State()
    #surname_2 = State()
    phone = State()
    inn = State()
    status = State()
