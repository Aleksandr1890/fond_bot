from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder

button_name = KeyboardButton(text='Имя')
button_surname = KeyboardButton(text='Фамилия')
button_surname_2 = KeyboardButton(text='Отчество')
button_phone = KeyboardButton(text='Телефон')
button_iin = KeyboardButton(text='ИИН')
button_status = KeyboardButton(text='Статус')

kb_account: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [button_name, button_surname, button_surname_2],
        [button_phone, button_iin, button_status]
    ],
    resize_keyboard=True
)


def send_phone() -> ReplyKeyboardMarkup:
    """function for sending a phone number during registration."""

    button_send_phone = KeyboardButton(
        text='Отправить телефон',
        request_contact=True
    )
    button_cancel = KeyboardButton(text='Отменить регистрацию')
    kb_send_phone: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [button_send_phone],
            [button_cancel]
        ],
        resize_keyboard=True
    )
    return kb_send_phone


def send_status() -> ReplyKeyboardMarkup:
    """function for sending a status during registration."""

    natural_person = KeyboardButton(
        text='Физическое лицо',
    )
    legal_person = KeyboardButton(text='ООО')
    self_employed = KeyboardButton(text='Самозанятый')
    individual_entrepreneur = KeyboardButton(text='ИП')
    kb_send_status: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [natural_person, self_employed],
            [individual_entrepreneur, legal_person]
        ],
        resize_keyboard=True
    )
    return kb_send_status
