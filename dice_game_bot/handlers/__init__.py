# -*- coding: utf-8 -*-
"""/dice_game_bot/handlers/__init__.py.

Объединяет все роутеры обработчиков в один - router_handlers.
"""

from typing import Final, List

from aiogram import Router

from . import start


__routers: Final[List[Router]] = [
    start.router
]
router_handlers: Router = Router(name="router_handlers")
router_handlers.include_routers(*__routers)
