from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from db.db_id import get_user, MyUser, add_user, get_register_user
from keyboards.keyboards_education import ikb_req_course
from keyboards.keyboards_grants import ikb_subsidies
from keyboards.keyboards_tax_and_lawyer import (
    main_keyboard,
    buh_legal_services,
    ikb_price_account, ikb_back_reg_tax
)
from lexicon.lexicon import LEXICON
from lexicon.lexicon_accountant import LEXICON_ACCOUNTANT
from lexicon.lexicon_register import LEXICON_REG

from lexicon.finance_start_lexicon import START

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        LEXICON[message.text],
        reply_markup=main_keyboard
    )
    user = message.from_user
    saved_user = await get_user(user.id, user.username)
    if not saved_user:
        new_user = MyUser(user.id, user.username)
        await add_user(new_user)
    await message.delete()


@router.callback_query(F.data == 'start')
async def process_second_start(callback: CallbackQuery):
    await callback.message.edit_text(
        LEXICON[f'/{callback.data}'],
        reply_markup=main_keyboard
    )


@router.callback_query(F.data == 'tax_register')
async def process_registration_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери услугу:',
        reply_markup=buh_legal_services
    )


@router.callback_query(F.data == 'reg_IP')
async def process_reg_ip_press(callback: CallbackQuery):
    text = LEXICON_REG[callback.data]
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_back_reg_tax
    )


@router.callback_query(F.data == 'legal_con')
async def process_reg_ip_press(callback: CallbackQuery):
    text = LEXICON_REG[callback.data]
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_back_reg_tax
    )


@router.callback_query(F.data == 'accountant_con')
async def process_reg_ip_press(callback: CallbackQuery):
    text = LEXICON_ACCOUNTANT[callback.data]
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_back_reg_tax
    )


@router.callback_query(F.data == 'accountant_service')
async def process_acc_ser(callback: CallbackQuery):
    text = LEXICON_ACCOUNTANT[callback.data]
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_price_account
    )


@router.callback_query(F.data == 'lawyer_service')
async def process_acc_ser(callback: CallbackQuery):
    text = LEXICON_REG[callback.data]
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_price_account
    )
