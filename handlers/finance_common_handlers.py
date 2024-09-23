from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.keyboards_grants import ikb_subsidies

router: Router = Router()


@router.callback_query(F.data == 'finance')
async def process_finance_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выберите поддержку:',
        reply_markup=ikb_subsidies
    )
