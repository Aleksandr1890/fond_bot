from aiogram.fsm.state import StatesGroup, State


class MessageStatesGroup(StatesGroup):
    subject = State()
    text_message = State()
    phone = State()
