from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

get_consultation = InlineKeyboardButton(
    text='Получить консультацию',
    callback_data='get_a_consultation'
)

back_legal_menu = InlineKeyboardButton(
    text='Назад',
    callback_data='tax_register'
)

ikb_price_account: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [get_consultation],
        [back_legal_menu],
    ]
)
