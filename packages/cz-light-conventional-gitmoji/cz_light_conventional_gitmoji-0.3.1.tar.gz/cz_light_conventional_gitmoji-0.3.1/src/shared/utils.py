"""
This module contains utility functions to work with Gitmoji objects.
"""

from typing import List

from shared.model import Gitmoji
from shared.spec import mojis

# global pattern to validate commit messages
PATTERN = (
    # To explicitly make . match new line
    r"(?s)"
    #  type
    r"^({type})"
    # scope
    r"(?:\((\S+)\))?!?: "
    # gitmoji and subject
    r"(({icon}) (?![\sA-Z])([^\n\r]+)(?<!\s))"
    # body
    r"(?:\r?\n\r?\n(?!\s)(.+)(?<!\s))?$"
)


def get_gitmojis() -> List[Gitmoji]:
    """Return the list of Gitmoji objects."""
    return [Gitmoji(**moji) for moji in mojis]


def get_type_pattern() -> str:
    """Return the type patterns."""
    return "|".join([moji.type for moji in get_gitmojis()])


def get_icon_pattern() -> str:
    """Return icon patterns."""
    return "|".join([moji.icon for moji in get_gitmojis()])


def get_pattern() -> str:
    """Return the complete validation pattern."""
    type_pattern = get_type_pattern()
    icon_pattern = get_icon_pattern()

    return PATTERN.replace("{type}", type_pattern).replace(
        "{icon}", icon_pattern
    )
