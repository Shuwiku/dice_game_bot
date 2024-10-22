# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from typing import Final, Optional

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data.models import User
from data.utils import add_user, get_user
from keyboards.reply import reply_to_menu
from locales.answer import (bot_brief_info,
                            user_already_registered,
                            user_register_failed,
                            user_registered_successfull)


router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Добавляет пользователя в базу данных, если его там нет.

    Добавляет пользователя в базу данных и приветствует его. Если
    пользователь уже зарегистрирован, то просто отвечает приветствием.
    В случае ошибки уведомляет пользователя.

    Если ошибки не произошло - прикрепляет клавиатуру с кнопкой ведущей
    в меню бота.

    Args:
        message (aiogram.types.Message): Данные о сообщении пользователя.
    """
    if not message.from_user:
        return None

    name: str = message.from_user.first_name
    uid: int = message.from_user.id
    user: Optional[User] = get_user(uid)

    if not user:

        if not add_user(uid, name):
            await message.answer(text=user_register_failed)
            return None

        answer: str = user_registered_successfull[:].format(name)
        await message.answer(text=answer)
        await message.answer(text=bot_brief_info, reply_markup=reply_to_menu)
        return None

    answer: str = user_already_registered[:].format(name)
    await message.answer(text=answer, reply_markup=reply_to_menu)
