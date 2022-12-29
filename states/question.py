from aiogram.dispatcher.filters.state import StatesGroup, State


class Question(StatesGroup):
    subject = State()
    topic = State()
    text = State()