from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    WebAppInfo

from data_for_change.start_finance import START_LINK

start_subsidies = InlineKeyboardButton(
    text='💵 Субсидии для начинающих бизнес',
    callback_data='start_finance'
)

active_subsidies = InlineKeyboardButton(
    text='💶 Субсидии для действующих предпринимателей',
    callback_data='active_finance'
)

back_main_menu = InlineKeyboardButton(
    text='🔙 Вернуться в главное меню',
    callback_data='start'
)

ikb_subsidies: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [start_subsidies],
        [active_subsidies],
        [back_main_menu],
    ]
)
