from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.paginator import paginator, CallbackPK
from lexicon.finance_active_lexicon import ACTIVE, ACTIVE_LINKS
#from lexicon.finance_start_lexicon import START, START_LINKS

router: Router = Router()


@router.callback_query(F.data == 'active_finance')
async def process_active_finance_press(callback: CallbackQuery):
    text = ACTIVE[1]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(ACTIVE), links=ACTIVE_LINKS, category='active')
    )


@router.callback_query(CallbackPK.filter(F.action == 'prev_active'))
async def process_active_prev_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page) - 1
    text = ACTIVE[page]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(ACTIVE), page, links=ACTIVE_LINKS, category='active')
    )


@router.callback_query(CallbackPK.filter(F.action == 'next_active'))
async def process_active_next_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page) + 1
    text = ACTIVE[page]
    await callback.message.edit_text(
        text=text,
        reply_markup=paginator(len(ACTIVE), page, links=ACTIVE_LINKS, category='active')
    )


@router.callback_query(CallbackPK.filter(F.action == 'current_active'))
async def process_active_current_page(
        callback: CallbackQuery,
        callback_data: CallbackPK,
):
    page = int(callback_data.page)
    await callback.answer(f'Страница {page} из {len(ACTIVE)}')
