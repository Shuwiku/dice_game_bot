# -*- coding: utf-8 -*-
"""Фильтр, проверяющий, есть ли пользователь в базе данных.

Нужен, чтобы избежать ошибок, если пользователь смог каким-либо образом
избежать использование команды "/start" при запуске бота.
"""

from aiogram.filters import Filter
from aiogram.types import Message

from data.utils import get_user
from locales.answer import user_not_registered


class IsUserRegistered(Filter):
    """Фильтр, проверяющий, есть ли пользователь в базе данных."""

    async def __call__(self, message: Message) -> bool:
        """Проверяет наличие пользователя в базе данных.

        Принимает входящее событие, создаёт сессию базы данных и по
        id пользователя из сообщения определяет его наличие в базе.

        В случае, если нет возможности получить id пользователя из
        сообщения, вернёт False.

        Args:
            message (aiogram.types.Message): Данные о сообщении пользователя.

        Returns:
            bool: Зарегистрирован пользователь или нет.
        """
        if message.from_user:
            if get_user(message.from_user.id):
                return True
            await message.answer(text=user_not_registered, reply_markup=None)
        return False
