from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


#запрос в БД, если 1, то X, если 0, то []

def give_event(data) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in ['conference', 'seminar', ]:
        mark = '[]' if data[button] == 0 else '[X]'
        kb_builder.row(InlineKeyboardButton(
            text=f'{mark} {button}',
            callback_data=f'{button} {mark}'))
    # Добавляем в конец клавиатуры кнопку "Отменить"
    #kb_builder.row(InlineKeyboardButton(
    #                    text=LEXICON['cancel'],
    #                    callback_data='cancel'))
    return kb_builder.as_markup()
