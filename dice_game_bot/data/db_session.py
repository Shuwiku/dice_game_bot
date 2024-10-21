# -*- coding: utf-8 -*-
"""Базовые функции для управления сессией базы данных."""

from typing import Optional, Final

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy.engine.base import Engine


base: Final = declarative_base()
__session: Optional[sessionmaker] = None


def create_session() -> Optional[Session]:
    """Возвращает сессию базы данных.

    Returns:
        sqlalchemy.orm.Session: Сессия базы данных.
        None: Если сессия не инициализирована (init_session).
    """
    return None if __session is None else __session()


def init(db_file_path: str) -> Optional[str]:
    """Запуск сессии базы данных.

    Args:
        db_file_path (str): Путь к файлу базы данных.

    Returns:
        str: Адрес подключения к базе данных.
        None: Если сессия уже была инициализирована.
    """
    global __session

    if __session:
        return None

    con_str: str = f"sqlite:///{db_file_path}?check_same_thread=False"
    engine: Final[Engine] = create_engine(con_str, echo=False)  # Запуск движка
    __session = sessionmaker(bind=engine)
    base.metadata.create_all(engine)  # Создаёт таблицы
    return con_str
