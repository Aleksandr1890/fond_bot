from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_main_menu = InlineKeyboardButton(
    text='🔙 Вернуться в главное меню',
    callback_data='start'
)

ikb_about_us: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_main_menu],
    ]
)
