from aiogram.types import (
    InlineKeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup
)

from data_for_change.education import COURSE_INTRO

req_intro = InlineKeyboardButton(
    text='🔗 Зарегистрироваться на курс',
    web_app=WebAppInfo(
        url=COURSE_INTRO
    )
)
schedule_intro = InlineKeyboardButton(
    text='🗓 График занятий',
    callback_data='schedule'
)
back_main_menu = InlineKeyboardButton(
    text='🔙 Вернуться в главное меню',
    callback_data='start'
)


ikb_req_course: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [req_intro],
        [schedule_intro],
        [back_main_menu],
    ]
)
