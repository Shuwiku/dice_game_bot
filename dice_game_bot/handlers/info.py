# -*- coding: utf-8 -*-
"""Обработчик кнопки/команды, выводящих информацию о боте."""

from typing import Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply import reply_to_menu
from locales.answer import bot_info
from locales.button import info


router: Final[Router] = Router(name=__name__)


@router.message(Command("info"))
@router.message(F.text == info)
async def btn_cmd_info(message: Message) -> None:
    """Отправляет сообщение с инфорацией о боте.

    Args:
        message (aiogram.types.Message): Данные о сообщении пользователя.
    """
    await message.answer(text=bot_info, reply_markup=reply_to_menu)
