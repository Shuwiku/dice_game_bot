# -*- coding: utf-8 -*-
"""Reply-клавиатура, отправляемая вместе с профилем пользователя."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from locales.button import menu, settings


_keyboard = [
    [KeyboardButton(text=settings),
     KeyboardButton(text=menu)]
]
reply_user_profile = ReplyKeyboardMarkup(keyboard=_keyboard,
                                         resize_keyboard=True)
