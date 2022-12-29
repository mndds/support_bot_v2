from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.support import support_keyboard, support_callback, check_support_available, get_support_manager, \
    cancel_support, cancel_support_callback
from loader import dp, bot


# @dp.callback_query_handler(text="accept_question")
# async def support_chat_access_btn_func(call: types.CallbackQuery, state: FSMContext):
#     support_id = int(call.from_user.id)
#     student_id = int(call.message.text.split(')\n')[0].split('(')[1])
#
#     await state.update_data(first_id=support_id)
#     await state.update_data(second_id=student_id)
#
#     await state.set_state("in_support")
#
#     await bot.send_message(support_id,
#                            "Вы на связи с пользователем!\n"
#                                   "Чтобы завершить общение нажмите на кнопку.",
#                            )
#     await bot.send_message( student_id,"Техподдержка на связи! Можете писать сюда свое сообщение. \nЧтобы завершить общение нажмите на кнопку.")
