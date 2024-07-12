from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

import bot
from fsm.fsm_send_message import MessageStatesGroup
from keyboards.keyboards_tax_and_lawyer import main_keyboard

router: Router = Router()


def send_phone() -> ReplyKeyboardMarkup:
    """function for sending a phone number during registration."""

    button_send_phone = KeyboardButton(
        text='Отправить телефон',
        request_contact=True
    )
    button_cancel = KeyboardButton(text='Отменить отправку')
    kb_send_phone: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [button_send_phone],
            [button_cancel]
        ],
        resize_keyboard=True
    )
    return kb_send_phone


def send_subject() -> ReplyKeyboardMarkup:
    """function for sending a subject of message."""

    subject_registration_ip_mfc = KeyboardButton(
        text='Составить заявление на регистрацию ИП',
    )
    subject_registration_ip_bank = KeyboardButton(
        text='Зарегистрировать ИП с открытием расчетного счета'
    )
    subject_registration_ooo = KeyboardButton(
        text='Подготовить документы для регистрации ООО'
    )
    kb_send_subject: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [subject_registration_ip_mfc],
            [subject_registration_ip_bank],
            [subject_registration_ooo],
        ],
        resize_keyboard=True
    )
    return kb_send_subject


@router.callback_query(
    F.data == 'get_a_consultation',
    StateFilter(default_state)
)
async def process_send_message(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(
        text='Укажите тему консультации или выберите из списка',
        reply_markup=send_subject()
    )

    await state.set_state(MessageStatesGroup.subject)


@router.message(StateFilter(MessageStatesGroup.subject))
async def process_text(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.delete()
    await message.answer(
        text='Спасибо!\n\nУкажите ваш вопрос:',
        #reply_markup=send_phone()
    )
    await state.set_state(MessageStatesGroup.text_message)


@router.message(StateFilter(MessageStatesGroup.text_message))
async def process_phone_message(message: Message, state: FSMContext):
    await state.update_data(text_message=message.text)
    await message.delete()
    await message.answer(
        text='Спасибо!\n\nУкажите ваш телефон, чтобы мы могли с вами связаться:',
        reply_markup=send_phone()
    )
    await state.set_state(MessageStatesGroup.text_message)


@router.message(StateFilter(MessageStatesGroup.status))
async def process_message_update(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.delete()
    data = await state.get_data()
    user = message.from_user
    await message.answer(
        text=f'Спасибо!\n\nСообщение отправлено!\n{data}',
        reply_markup=main_keyboard
    )
    await router.

    await state.clear()
