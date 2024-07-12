from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)

from data_for_change.links import LINK_ACCOUNTANT, LINK_LAWYER

tax_and_registration = InlineKeyboardButton(
    text='Налоги и регистрация бизнеса',
    callback_data='tax_register')

subsidy = InlineKeyboardButton(
    text='Субсидии и гранты',
    callback_data='finance')

course = InlineKeyboardButton(
    text='Бесплатный курс "Введение в предпринимательство"',
    callback_data='edu')

loan = InlineKeyboardButton(
    text='Займы для бизнеса',
    callback_data='loan')

about_fund = InlineKeyboardButton(
    text='О Фонде',
    callback_data='about_us')

main_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [tax_and_registration],
        [subsidy],
        [course],
        [loan],
        [about_fund]
    ]
)

#registration_and_tax

registration = InlineKeyboardButton(
    text='👔 Зарегистрировать самозанятость, ИП или ООО',
    callback_data='reg_IP')

legal_consultation = InlineKeyboardButton(
    text='💬 Получить юридическую консультацию',
    callback_data='legal_con')

accountant_consultation = InlineKeyboardButton(
    text='💬 Получить консультацию бухгалтера',
    callback_data='accountant_con')

accountant_services = InlineKeyboardButton(
    text='📝 Заполнить налоговую отчетность',
    callback_data='accountant_service')

back_to_main = InlineKeyboardButton(
    text='Вернуться в главное меню',
    callback_data='start')

buh_legal_services: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [registration],
        [accountant_services],
        [legal_consultation],
        [accountant_consultation],
        [back_to_main],
    ]
)

price_account = InlineKeyboardButton(
    text='Узнать стоимость бухгалтерских услуг',
    web_app=WebAppInfo(
        url=LINK_ACCOUNTANT
    )
)
price_lawyer = InlineKeyboardButton(
    text='Узнать стоимость юридических услуг',
    web_app=WebAppInfo(
        url=LINK_LAWYER
    )
)
back_legal_menu = InlineKeyboardButton(
    text='Назад',
    callback_data='tax_register'
)


ikb_price_account: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [price_account],
        [price_lawyer],
        [back_legal_menu],
    ]
)

ikb_back_reg_tax: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_legal_menu],
    ]
)
