from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        if (message.chat.type != 'private'):
            await message.answer('Данную команду можно использовать только в личных сообщениях с ботом.')
            return
        else:
            await message.answer(f"Привет, {message.from_user.full_name}! Я помогу решить ваш вопрос! Выберите действие")
    except Exception as e:
        await message.answer(f"Упс! *Ошибка!* Не переживайте, ошибка уже *отправлена* разработчику.", parse_mode='Markdown')

