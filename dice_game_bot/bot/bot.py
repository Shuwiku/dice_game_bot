# -*- coding: utf-8 -*-
"""Инструменты для создания и получения объектов бота и диспетчера."""

from aiogram import Bot, Dispatcher

from handlers import router_handlers


__bot: Bot
__dispatcher: Dispatcher


def __include_routers() -> None:
    """Добавляет все роутеры в диспетчер."""
    global __dispatcher

    __dispatcher.include_router(router_handlers)


def get_bot() -> Bot:
    """Возвращает объект бота.

    Returns:
        aiogram.Bot: Объект бота aiogram.
    """
    return __bot


def get_dispatcher() -> Dispatcher:
    """Возвращает объект диспетчера.

    Returns:
        aiogram.Dispatcher: Объект диспетчера aiogram.
    """
    return __dispatcher


def init(bot_token: str) -> None:
    """Создаёт и настраивает объекты бота и диспетчера.

    Args:
        bot_token (str): Токен телеграм бота.
    """
    global __bot, __dispatcher

    __bot = Bot(bot_token)
    __dispatcher = Dispatcher()
    __include_routers()
