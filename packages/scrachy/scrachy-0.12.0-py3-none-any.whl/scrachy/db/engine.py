#  Copyright 2023 Reid Swanson.
#
#  This file is part of scrachy.
#
#  scrachy is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  scrachy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with scrachy.  If not, see <https://www.gnu.org/licenses/>.

"""
Utilities to initialize and work with the SqlAlchemy engine.
"""

# Python Modules
import logging

from contextlib import contextmanager
from typing import Optional

# 3rd Party Modules
from scrapy.settings import Settings
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.ddl import CreateSchema

# Project Modules
from scrachy.db.base import Base
from scrachy.utils.db import construct_url


log = logging.getLogger(__name__)


# Singleton engine for the project. However, it is the responsibility
# of the AlchemyCacheStorage to initialize it on construction.
engine: Optional[Engine] = None
session_factory: Optional[sessionmaker] = None


def initialize_engine(settings: Settings):
    global engine
    global session_factory

    if engine is not None:
        return  # The engine is already setup

    schema = settings.get('SCRACHY_DB_SCHEMA')
    connect_args = settings.get('SCRACHY_DB_CONNECT_ARGS')

    # Create the engine
    execution_options = {"schema_translate_map": {None: schema}} if schema else None
    engine = create_engine(
        construct_url(settings),
        connect_args=connect_args,
        execution_options=execution_options
    )

    # Create the schema if necessary
    if schema is not None:
        with engine.connect() as connection:
            connection.execute(CreateSchema(schema, if_not_exists=True))
            connection.commit()

    # Create the tables if necessary
    Base.metadata.create_all(engine)

    # Create a session factory
    session_factory = sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    return engine


def reset_engine():
    global engine
    global session_factory

    if engine is not None:
        engine.dispose()

    if session_factory is not None:
        session_factory.close_all()

    engine = None
    session_factory = None


@contextmanager
def session_scope():
    if session_factory is None:
        raise ValueError("You must initialize the engine first.")

    session = session_factory()

    # noinspection PyBroadException
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
