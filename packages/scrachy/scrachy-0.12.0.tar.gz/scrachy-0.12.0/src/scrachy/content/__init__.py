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
Classes and utilities for extracting textual content from the HTML body.
"""

# Python Modules
from typing import Protocol

from scrapy.settings import Settings


# 3rd Party Modules

# Project Modules


class ContentExtractor(Protocol):
    def get_content(self, html: str) -> str:
        """
        Get the desired textual content from the HTML.

        :param html: The textual HTML to process.
        :return: The desired content (e.g., text with tags removed).
        """
        pass


class BaseContentExtractor(ContentExtractor):
    def __init__(self, settings: Settings):
        """
        A content extractor base class that keeps track of the project
        middleware.

        :param settings: The Scrapy ``Settings``.
        """
        super().__init__()

        self.settings = settings
