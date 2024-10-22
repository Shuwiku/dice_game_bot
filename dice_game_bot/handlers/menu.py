# -*- coding: utf-8 -*-
"""Обработчик кнопки/команды, выводящих меню бота."""

from typing import Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply import reply_bot_menu
from locales.answer import bot_menu
from locales.button import menu


router: Final[Router] = Router(name=__name__)


@router.message(Command("menu"))
@router.message(F.text == menu)
async def btn_cmd_menu(message: Message) -> None:
    """Отправляет сообщение с меню бота с пояснениями.

    Args:
        message (aiogram.types.Message): Данные о сообщении пользователя.
    """
    await message.answer(text=bot_menu, reply_markup=reply_bot_menu)
