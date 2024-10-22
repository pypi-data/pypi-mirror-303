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
The SqlAlchemy models.
"""

from __future__ import annotations

# Python Modules
from typing import Optional

# 3rd Party Modules
import sqlalchemy
import sqlalchemy.orm

from sqlalchemy import ColumnElement, String, ForeignKey, type_coerce
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Project Modules
from scrachy.db.base import Base, binary, conditional_json, smallint, timestamp


# Primary tables
class Response(Base):
    """
    Stores the minimum amount of information to recreate the html of a
    page given its request fingerprint. The cache only stores the most
    recent version of the page, but the :class:`ScrapyHistory` table
    can be used to view

    Additional data is stored in other tables, but can be accessed via
    relationships.
    """
    # A hash of the page's uniquely identifying request information.
    fingerprint: Mapped[binary] = mapped_column(primary_key=True)

    # The most recent timestamp when the page was scraped.
    scrape_timestamp: Mapped[timestamp] = mapped_column(default=None)

    # This is redundant with the request, but can prevent a join when
    # we might want to search or filter responses by it.
    url: Mapped[str] = mapped_column(index=True)

    # The request method (True for GET. False for POST)
    method: Mapped[bool] = mapped_column(default=None)

    # The body of the request (primarily used for POST requests)
    request_body: Mapped[Optional[binary]] = mapped_column(default=None)

    # The response body
    body: Mapped[binary] = mapped_column(default=None)

    # Store the metadata associated with the response as JSON.
    meta: Mapped[Optional[conditional_json]] = mapped_column(default=None)

    # The response status code for the page
    status: Mapped[Optional[smallint]] = mapped_column(default=None)

    # The response headers
    headers: Mapped[Optional[str]] = mapped_column(default=None)

    # The text of the response stripped of HTML and possibly stripped of
    # boilerplate content.
    extracted_text: Mapped[Optional[str]] = mapped_column(default=None)

    # The number of bytes of the full downloaded response (including the HTML)
    body_length: Mapped[int]

    # The number of bytes of the response excluding the HTML.
    extracted_text_length: Mapped[Optional[int]] = mapped_column(default=None)

    # The scrape history
    scrape_history: Mapped[list[ScrapeHistory]] = relationship(
        cascade='all, delete-orphan',
        default_factory=list,
        repr=False
    )

    # I believe hybrid properties allow changing how the property behaves
    # depending on whether you are using it as an instance or as a class
    # template. For example, when operating on an instance referencing the
    # `body` property will use the regular python code in the method body.
    # But if you using it as a template for SQL operations you can define
    # a @xxx.inplace.expression method that will use the same property name
    # but emit SQL code instead.

    # So here, for example, it uses less space to store the request method
    # as a boolean (because it can only ever have two values), but it is
    # more convenient to work with these values as their original string
    # representations.
    @hybrid_property
    def request_method(self) -> Optional[str]:
        """
        Get the request method as a string instead of the stored boolean
        type.
        """
        if self.method is True:
            return 'GET'
        elif self.method is False:
            return 'POST'

        return None

    @request_method.inplace.setter
    def request__method(self, method: str) -> None:
        """
        Client side setter.

        :param method:
        :return:
        """
        self.method = method.upper() == 'GET'  # noqa

    # noinspection PyMethodParameters,PyNestedDecorators
    @request_method.inplace.expression
    @classmethod
    def request_method(cls) -> ColumnElement[Optional[str]]:
        """
        Server side setter.

        :return:
        """
        return type_coerce(
            sqlalchemy.case(
                (cls.method == True, 'GET'),
                (cls.method == False, 'POST'),
            ),
            String
        )


class ScrapeHistory(Base):
    """
    Store the history of when a page was scraped.
    """
    fingerprint: Mapped[binary] = mapped_column(ForeignKey('response.fingerprint'), primary_key=True)

    # When the page was scraped
    scrape_timestamp: Mapped[timestamp] = mapped_column(primary_key=True)

    # The response body
    body: Mapped[binary]
