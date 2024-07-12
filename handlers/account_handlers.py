from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.db_id import get_register_user, get_events_data
from keyboards.kb_newsletter import give_event
from keyboards.keyboards_account import kb_account
from lexicon.lexicon_account import LEXICON

router: Router = Router()


@router.message(Command(commands='account'))
async def process_account_command(message: Message):
    if await get_register_user(message.from_user.id):
        data = await get_events_data(message.from_user.id)
        await message.answer(
            text=LEXICON['/account'],
            reply_markup=give_event(data)
        )
    else:
        await message.answer(
            text='Аккаунт не зарегистрирован. Нажмите "Зарегистрировать '
            'аккаунт для доступа к личному кабинету."',
            #reply_markup=kb_account
        )
