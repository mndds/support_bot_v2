from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.question import Question


@dp.message_handler(Command("ask"))
async def set_subject(message: types.Message):
    await message.answer("Напишите предмет:")
    await Question.subject.set()


@dp.message_handler(state=Question.subject)
async def set_topic(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(subject=answer)
    await message.answer("Напишите название темы:")
    await Question.topic.set()


@dp.message_handler(state=Question.topic)
async def set_text(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(topic=answer)
    await message.answer("Напишите вопрос:")
    await Question.text.set()
