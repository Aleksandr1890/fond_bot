from aiogram.types import (
    InlineKeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup
)

from data_for_change.loan import (
    LINK_SCHEDULE,
    LINK_DOCUMENTS_IP,
    LINK_DOCUMENTS_OOO
)

schedule_loan_button = InlineKeyboardButton(
    text='📊 Рассчитать график платежей',
    web_app=WebAppInfo(
        url=LINK_SCHEDULE
    )
)
ip_documents = InlineKeyboardButton(
    text='📄 Скачать документы для займа для ИП',
    web_app=WebAppInfo(
        url=LINK_DOCUMENTS_IP
    )
)
ooo_documents = InlineKeyboardButton(
    text='📄 Скачать документы для займа для ООО',
    web_app=WebAppInfo(
        url=LINK_DOCUMENTS_OOO
    )
)
back_main_menu = InlineKeyboardButton(
    text='🔙 Вернуться в главное меню',
    callback_data='start'
)

ikb_loan: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [schedule_loan_button],
        [ip_documents],
        [ooo_documents],
        [back_main_menu],
    ]
)
