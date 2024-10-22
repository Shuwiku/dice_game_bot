# -*- coding: utf-8 -*-
"""Dice Game Bot - телеграм-бот для игры в кости за виртуальную валюту.

Создан с использованием фреймворка aiogram для взаимодействия с пользователем
и библиотеки SQLAlchemy для хранения данных.

В будущем планируется создание более крупного бота - Casino Game Bot, в
которого будет интегрирован функционал этого бота.

Автор: Shuwiku (shuwiku@gmail.com)
GitHub: github.com/Shuwiku/dice_game_bot
Лицензия: MIT License
"""

import asyncio
import os

from dotenv import load_dotenv

import bot
import data


BOT_TOKEN: str
DATABASE_FILE: str


def _load_env() -> None:
    """Загружает переменные окружения из .env."""
    global BOT_TOKEN, DATABASE_FILE

    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # pyright: ignore
    DATABASE_FILE = os.getenv("DATABASE_FILE")  # pyright: ignore

    if not any([BOT_TOKEN, DATABASE_FILE]):
        raise ValueError("[X] Не все переменные окружения указаны!")


async def main() -> None:
    """Настраивает и запускает бота."""
    global BOT_TOKEN, DATABASE_FILE

    _load_env()
    print("[#] Переменные окружения загружены.")

    data.init(DATABASE_FILE)
    print("[#] Сессия базы данных инициализирована.")

    bot.init(BOT_TOKEN)
    print("[#] Запуск диспетчера...")

    await bot.get_dispatcher().start_polling(bot.get_bot())


if __name__ == "__main__":
    asyncio.run(main())
