from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import CallbackQuery, Message

import db.db_id
from fsm.fsm_register import UserStatesGroup
from keyboards.keyboards_account import send_phone, send_status
from keyboards.keyboards_tax_and_lawyer import main_keyboard

router: Router = Router()


@router.message(Command(commands='register'), StateFilter(default_state))
async def process_register(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(
        text='Напишите фамилию, имя и отчество (при наличии) через пробел: '
             '(пример: Иванов Иван Иванович)',
        #reply_markup=get_cancel_kb()
    )

    await state.set_state(UserStatesGroup.name)


@router.message(StateFilter(UserStatesGroup.name))
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.delete()
    await message.answer(
        text='Спасибо!\n\nУкажите ваш телефон:',
        reply_markup=send_phone()
    )
    await state.set_state(UserStatesGroup.phone)


@router.message(StateFilter(UserStatesGroup.phone))
async def process_phone(message: Message, state: FSMContext):
    contact = message.text if message.text else message.contact.phone_number
    await state.update_data(phone=contact)
    await message.delete()
    await message.answer(
        text='Спасибо!\n\nУкажите ваш ИНН:',
    )
    await state.set_state(UserStatesGroup.inn)


@router.message(StateFilter(UserStatesGroup.inn))
async def process_inn(message: Message, state: FSMContext):
    await state.update_data(inn=message.text)
    await message.delete()
    await message.answer(
        text='Спасибо!\n\nУкажите ваш статус:',
        reply_markup=send_status()
    )
    await state.set_state(UserStatesGroup.status)


@router.message(StateFilter(UserStatesGroup.status))
async def process_status(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.delete()
    data = await state.get_data()
    user = message.from_user
    #saved_user = await db.db_id.get_user(user.id, user.username)
    saved_user = db.db_id.MyUser(
        user.id, user.username, name=data['name'], phone=data['phone'],
        inn=data['inn'], status=data['status'], register=True
    )
    await db.db_id.register_user(saved_user, user.id)
    await message.answer(text=f'Спасибо!\n\nРегистрация завершена!\n{data}',
                         reply_markup=main_keyboard)

    await state.clear()
