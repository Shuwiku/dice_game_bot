# -*- coding: utf-8 -*-
"""Обработчик команды/кнопки, выводящих профиль пользователя.

Анализаторы кода ругаются на часть кода, т.к функция data.utils.get_user()
возвращает Optional[User], т.е вместо data.models.User может оказаться None.
Однако, на входе в обработчик стоит фильтр filters.IsUserRegistered(), который
не даст зайти незарегистрированному пользователю в обработчик, следовательно
get_user() точно вернет User. Чтобы избежать засорения кода комментариями
"# pyright: ignore" я решил всё же сделать проверку if user, хотя она тут
не нужна.
"""

from typing import Any, Final, Optional

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from data.models import User
from data.utils import get_user
from filters import IsUserRegistered
from keyboards.reply import reply_user_profile
from locales.answer import user_profile
from locales.button import profile


router: Final[Router] = Router(name=__name__)


@router.message(Command("profile"), IsUserRegistered())
@router.message(F.text == profile, IsUserRegistered())
async def cmd_txt_menu(message: Message) -> None:
    """Отправляет в ответ сообщение с профилем пользователя.

    Args:
        message (aiogram.types.Message): Данные о сообщении пользователя.
    """
    if not message.from_user:
        return None

    uid: int = message.from_user.id
    user: Optional[User] = get_user(uid)

    if user:

        winrate: Any[float, int] = 0
        if user.dice_played != 0:  # pyright: ignore
            winrate = user.dice_won / user.dice_played

        data: list = [user.name, user.balance, user.diamonds,
                      user.dice_won, winrate]
        answer = user_profile[:].format(*data)
        await message.answer(text=answer, reply_markup=reply_user_profile)
