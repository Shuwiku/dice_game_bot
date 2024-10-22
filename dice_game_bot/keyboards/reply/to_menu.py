# -*- coding: utf-8 -*-
"""Reply-клавиатура с кнопкой, ведущей в меню бота."""

from typing import Final, List

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from locales.button import menu


__keyboard: List[List[KeyboardButton]] = [
    [KeyboardButton(text=menu)]
]
reply_to_menu: Final = ReplyKeyboardMarkup(keyboard=__keyboard,
                                           resize_keyboard=True)
