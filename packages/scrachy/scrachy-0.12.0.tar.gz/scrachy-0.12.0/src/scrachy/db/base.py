#  Copyright 2020 Reid Swanson.
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
The basic data types and classes required to define the SqlAlchemy models.
"""

from __future__ import annotations

# Python Modules
import logging

from typing import Annotated

# 3rd Party Modules
from sqlalchemy import MetaData, BigInteger, LargeBinary, SmallInteger
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, declared_attr

# Project Modules
from scrachy.settings import PROJECT_SETTINGS
from scrachy.utils.sqltypes import ConditionalJson, TimeStampTZ
from scrachy.utils.strings import camel_to_snake

bigint = Annotated[BigInteger, 64]
binary = Annotated[LargeBinary, None]
smallint = Annotated[int, 16]
timestamp = Annotated[TimeStampTZ, None]
conditional_json = Annotated[ConditionalJson, None]

log = logging.getLogger(__name__)


schema = PROJECT_SETTINGS.get('SCRACHY_DB_SCHEMA')
schema_prefix = f"{schema}." if schema else ""


class Base(DeclarativeBase, MappedAsDataclass, kw_only=True, eq=True, unsafe_hash=False):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
        schema=schema
    )

    type_annotation_map = {
        bigint: BigInteger,
        binary: LargeBinary,
        conditional_json: ConditionalJson,
        smallint: SmallInteger,
        timestamp: TimeStampTZ(timezone=True),
    }

    # noinspection PyMethodParameters
    @declared_attr
    def __tablename__(cls):
        return camel_to_snake(cls.__name__)
