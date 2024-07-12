from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.keyboards_about_us import ikb_about_us
from lexicon.lexicon_about_us import LEXICON_ABOUT

router: Router = Router()


@router.callback_query(F.data == 'about_us')
async def process_about_press(callback: CallbackQuery):
    text = LEXICON_ABOUT['opening']
    await callback.message.edit_text(
        text=text,
        reply_markup=ikb_about_us
    )
