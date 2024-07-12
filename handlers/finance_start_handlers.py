from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.paginator import paginator, CallbackPK
from lexicon.finance_start_lexicon import START, START_LINKS

router: Router = Router()


@router.callback_query(F.data == 'start_finance')
async def process_start_finance_press(callback: CallbackQuery):
    text = START[1]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(START), links=START_LINKS, category='start')
    )


@router.callback_query(CallbackPK.filter(F.action == 'prev_start'))
async def process_prev_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page) - 1
    text = START[page]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(START), page, links=START_LINKS, category='start')
    )


@router.callback_query(CallbackPK.filter(F.action == 'next_start'))
async def process_next_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page) + 1
    text = START[page]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(START), page, links=START_LINKS, category='start')
    )


@router.callback_query(CallbackPK.filter(F.action == 'current_start'))
async def process_current_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page)
    await callback.answer(f'Страница {page} из {len(START)}')
