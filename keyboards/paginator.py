from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    WebAppInfo


class CallbackPK(CallbackData, prefix='my'):
    action: str
    page: int


def paginator(
        len_dict: int,
        page: int = 1,
        links: dict = None,
        category: str = None
) -> InlineKeyboardMarkup:
    prev_element = InlineKeyboardButton(
        text='⬅',
        callback_data=CallbackPK(action=f'prev_{category}', page=page).pack()
    )
    count_elements = InlineKeyboardButton(
        text=f'{page}/{len_dict}',
        callback_data=CallbackPK(
            action=f'current_{category}', page=page
        ).pack()
    )
    download_docs = InlineKeyboardButton(
        text='📄 Подробнее',
        web_app=WebAppInfo(
            url=links[page]
        )
    )
    next_element = InlineKeyboardButton(
        text='➡',
        callback_data=CallbackPK(action=f'next_{category}', page=page).pack()
    )

    back_finance_menu = InlineKeyboardButton(
        text='Назад',
        callback_data='finance'
    )

    ikb_paginator_full: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [download_docs],
            [prev_element, count_elements, next_element],
            [back_finance_menu],
        ]
    )
    ikb_paginator_left: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [download_docs],
            [prev_element, count_elements],
            [back_finance_menu],
        ]
    )
    ikb_paginator_right: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [download_docs],
            [count_elements, next_element],
            [back_finance_menu],
        ]
    )
    if 1 < page < len_dict:
        return ikb_paginator_full
    elif page == 1:
        return ikb_paginator_right
    else:
        return ikb_paginator_left
