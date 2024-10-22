# -*- coding: utf-8 -*-
"""Reply-клавиатура, отправляемая вместе с меню бота."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from locales.button import profile, play, info


_keyboard = [
    [KeyboardButton(text=profile),
     KeyboardButton(text=play),
     KeyboardButton(text=info)]
]
reply_bot_menu = ReplyKeyboardMarkup(keyboard=_keyboard, resize_keyboard=True)
