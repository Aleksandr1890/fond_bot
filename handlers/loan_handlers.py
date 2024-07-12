from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.keyboards_loan import ikb_loan
from lexicon.lexicon_loan import LEXICON_LOAN

router: Router = Router()


@router.callback_query(F.data == 'loan')
async def process_loan_press(callback: CallbackQuery):
    text = LEXICON_LOAN['loan']
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_loan
    )
