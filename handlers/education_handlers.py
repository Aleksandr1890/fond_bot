from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.keyboards_education import ikb_req_course
from lexicon.lexicon_education import LEXICON_EDU

router: Router = Router()


@router.callback_query(F.data == 'edu')
async def process_edu_press(callback: CallbackQuery):
    text = LEXICON_EDU['edu_intro']
    await callback.message.answer(
        text=text,
        reply_markup=ikb_req_course
    )


@router.callback_query(F.data == 'schedule')
async def process_edu_press(callback: CallbackQuery):
    text = LEXICON_EDU['schedule_intro']
    await callback.message.answer(
        text=text,
        reply_markup=ikb_req_course
    )
