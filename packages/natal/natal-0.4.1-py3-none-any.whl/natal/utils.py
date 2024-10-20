"""utility functions for natal"""

from datetime import datetime
from natal.config import Config
from types import SimpleNamespace
from typing import Any, Iterable, Mapping


class DotDict(SimpleNamespace, Mapping):
    """
    Extends SimpleNamespace to allow for unpacking and subscript notation access.
    """

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __iter__(self):
        return iter(self.__dict__.keys())

    def __len__(self):
        return len(self.__dict__)


def color_hex(name: str, config: Config = Config()) -> str:
    """
    Get color hex from name and Config instance, default to 'natal_config.yml'.

    Args:
        name (str): The name of the color.
        config (Config): The configuration instance.

    Returns:
        str: The hex value of the color.
    """
    return getattr(config.colors, name)


def pairs[T](iterable: Iterable[T]) -> list[tuple[T, T]]:
    """
    Generate pairs of elements from an iterable.

    Args:
        iterable (Iterable[T]): The input iterable.

    Returns:
        list[tuple[T, T]]: A list of tuples, each containing a pair of elements.
    """
    output = []
    for i in range(len(iterable)):
        for j in range(i + 1, len(iterable)):
            output.append((iterable[i], iterable[j]))
    return output


def member_of[T](const: list[T], name: str) -> T:
    """
    Get a member from a list of constants by name.

    Args:
        const (list[T]): The list of constants.
        name (str): The name of the member.

    Returns:
        T: The member with the specified name.
    """
    idx: int = const["name"].index(name)
    return {prop: const[prop][idx] for prop in const.model_fields}


def str_to_dt(dt_str: str) -> datetime:
    """
    Convert a string to a datetime object.

    Args:
        dt_str (str): The datetime string.

    Returns:
        datetime: The corresponding datetime object.
    """
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
