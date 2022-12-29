from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import cfg
from keyboards.inline.support_chat import support_chat_kb
from loader import dp, bot

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
from states.question import Question


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


@dp.message_handler(state=Question.text)
async def bot_echo_support_chat(message: types.Message, state: FSMContext):
    data = await state.get_data()
    subject = data.get("subject")
    topic = data.get("topic")
    text = message.text
    await state.finish()
    await message.answer("Ваш вопрос был отправлен!\nОжидайте ответа!")
    await bot.send_message(cfg['support_chat_id'], f"✉ | Новый вопрос\n👤 От: @{message.chat.username}({message.from_user.id})\n📚 Предмет: {subject}\n🔴 Тема:{topic}\n\n❓ Вопрос: {text}",reply_markup=support_chat_kb)





# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
