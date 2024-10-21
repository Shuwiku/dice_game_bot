# -*- coding: utf-8 -*-
"""Функция для добавления пользователя в базу данных."""

from typing import Optional

from sqlalchemy.orm import Session

from ..db_session import create_session
from ..models import User


def add_user(uid: int, name: str) -> bool:
    """Добавляет объект пользователя в базу данных.

    Args:
        uid (int): ID пользователя.
        name (str): Имя пользователя.

    Returns:
        bool: True, если пользователь добавлен, иначе False.
    """
    session: Optional[Session] = create_session()
    if session:
        user: User = User(uid=uid, name=name)
        session.add(user)
        session.commit()
        return True
    return False
