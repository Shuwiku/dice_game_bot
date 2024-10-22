# -*- coding: utf-8 -*-
"""Обработчики событий бота."""

from typing import Final, List

from aiogram import Router

from . import (info,
               menu,
               profile,
               start)


__routers: Final[List[Router]] = [info.router,
                                  menu.router,
                                  profile.router,
                                  start.router]
router_handlers: Router = Router(name="router_handlers")
router_handlers.include_routers(*__routers)
