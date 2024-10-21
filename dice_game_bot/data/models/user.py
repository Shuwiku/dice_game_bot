# -*- coding: utf-8 -*-
"""Таблица для пользователя SQLAlchemy."""

from typing import Final

from sqlalchemy import Column, Integer, String

from data.db_session import base


class User(base):
    """Таблица для пользователя SQLAlchemy.

    Args:
        uid (int): ID пользователя.
        name (str): Имя пользователя.
        balance (int): Баланс (деньги на счету у) пользователя.
        diamonds (int): Кол-во алмазов у пользователя.
        dice_played (int): Кол-во игр, сыгранных в кости.
        dice_won (int): Кол-во игр, выиграных в кости.
    """

    __tablename__: str = "users"

    uid: Final[Column[int]] = Column(Integer, primary_key=True)
    name: Final[Column[str]] = Column(String, nullable=False)
    balance: Final[Column[int]] = Column(Integer, default=1000)
    diamonds: Final[Column[int]] = Column(Integer, default=10)
    dice_played: Final[Column[int]] = Column(Integer, default=0)
    dice_won: Final[Column[int]] = Column(Integer, default=0)
