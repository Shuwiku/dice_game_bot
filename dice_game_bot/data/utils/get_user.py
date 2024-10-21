# -*- coding: utf-8 -*-
"""Функция для получения объекта пользователя по его id из базы данных."""

from typing import Optional

from sqlalchemy.orm import Session

from ..db_session import create_session
from ..models import User


def get_user(user_id: int) -> Optional[User]:
    """Возвращает объект пользователя по его id.

    Если пользователя нет или сессия базы данных не определена - вернёт None. 

    Args:
        user_id (int): id пользователя.
        None: Если сессия не определена или пользователя нет в базе.

    Returns:
        Optional[User]: Объект пользователя или None.
    """
    session: Optional[Session] = create_session()
    if session:
        user: Optional[User]
        user = session.query(User).filter(User.uid == user_id).first()
        return user
    return None
