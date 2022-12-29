import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.config import support_ids
from loader import dp

support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")

support_chat_kb = InlineKeyboardMarkup()
accept_btn = InlineKeyboardButton(text='Принять запрос', callback_data="accept_question")
support_chat_kb.insert(accept_btn)

