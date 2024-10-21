"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from contextlib import suppress
from re import compile
from re import match as re_match
from typing import Any
from typing import Optional
from typing import Union

from .empty import Empty
from .types import DictStrAny



_INTEGER = compile(r'^\d+$')
_INDICES = (list, tuple, dict)
_RECURSE = dict



_SETABLE = Union[
    DictStrAny,
    list[Any]]

_GETABLE = Union[
    tuple[Any, ...],
    _SETABLE]



def getate(
    source: _GETABLE,
    path: str,
    default: Optional[Any] = None,
    delim: str = '/',
) -> Any:  # noqa: ANN401
    """
    Collect the value within the dictionary using notation.

    Example
    -------
    >>> source = {'foo': {'bar': 'baz'}}
    >>> getate(source, 'foo/bar')
    'baz'

    Example
    -------
    >>> source = {'foo': ['bar', 'baz']}
    >>> getate(source, 'foo/1')
    'baz'

    :param source: Dictionary object processed in notation.
    :param path: Path to the value within the source object.
    :param default: Value to use if none is found in source.
    :param delim: Override default delimiter between parts.
    :returns: Value that was located within provided source.
    """

    sourze: Any = source

    split = path.split(delim)

    length = len(split)


    items = enumerate(split)

    for index, base in items:

        if sourze is Empty:
            return default


        indices = isinstance(
            sourze, _INDICES)

        if (indices is False
                and index < length):
            return default


        recurse = isinstance(
            sourze, _RECURSE)

        if recurse is False:

            with suppress(IndexError):
                sourze = sourze[int(base)]
                continue


        if base not in sourze:
            sourze = Empty
            continue

        sourze = sourze[base]


    return (
        default if sourze is Empty
        else sourze)



def setate(
    source: _SETABLE,
    path: str,
    value: Any,  # noqa: ANN401
    delim: str = '/',
) -> None:
    """
    Define the value within the dictionary using notation.

    Example
    -------
    >>> source = {'foo': {'bar': 'baz'}}
    >>> source['foo']['bar']
    'baz'
    >>> setate(source, 'foo/bar', 'bop')
    >>> source['foo']['bar']
    'bop'

    :param source: Dictionary object processed in notation.
    :param path: Path to the value within the source object.
    :param value: Value which will be defined at noted point.
    :param delim: Override default delimiter between parts.
    """

    _setvalue(source, path, value, delim)



def delate(
    source: _SETABLE,
    path: str,
    delim: str = '/',
) -> None:
    """
    Delete the value within the dictionary using notation.

    Example
    -------
    >>> source = {'foo': {'bar': 'baz'}}
    >>> delate(source, 'foo/bar')
    >>> source
    {'foo': {}}

    :param source: Dictionary object processed in notation.
    :param path: Path to the value within the source object.
    :param delim: Override default delimiter between parts.
    """

    split = path.split(delim)

    with suppress(KeyError, IndexError):


        for part in split[:-1]:

            setable = isinstance(
                source, dict | list)

            if setable is False:
                raise ValueError('source')

            if isinstance(source, list):
                source = source[int(part)]

            elif isinstance(source, dict):
                source = source[part]


        part = split[-1]

        setable = isinstance(
            source, dict | list)

        if setable is False:
            raise ValueError('source')

        if isinstance(source, dict):
            del source[part]

        if isinstance(source, list):
            del source[int(part)]



def _setpath(
    source: _SETABLE,
    path: str,
    value: Any,  # noqa: ANN401
    delim: str = '/',
) -> None:
    """
    Define the value within the dictionary using notation.

    .. note::
       This is a private helper function that could change.

    :param source: Dictionary object processed in notation.
    :param path: Path to the value within the source object.
    :param value: Value which will be defined at noted point.
    :param delim: Override default delimiter between parts.
    """


    setable = isinstance(
        source, dict | list)

    assert setable is True


    base, path = (
        path.split(delim, 1))

    next = (
        path.split(delim, 1)[0])


    default: _SETABLE = {}

    if re_match(_INTEGER, next):
        default = []

    update: Any


    if isinstance(source, list):

        length = len(source)
        index = int(base)

        update = default

        with suppress(IndexError):
            update = source[index]

        _setvalue(
            update, path,
            value, delim)

        if length == index:
            source.append(update)

        elif length > index:
            source[index] = update


    elif isinstance(source, dict):

        update = default

        with suppress(KeyError):
            update = source[base]

        _setvalue(
            update, path,
            value, delim)

        source[base] = update



def _setvalue(
    source: _SETABLE,
    path: str,
    value: Any,  # noqa: ANN401
    delim: str = '/',
) -> None:
    """
    Define the value within the dictionary using notation.

    .. note::
       This is a private helper function that could change.

    :param source: Dictionary object processed in notation.
    :param path: Path to the value within the source object.
    :param value: Value which will be defined at noted point.
    :param delim: Override default delimiter between parts.
    """


    setable = isinstance(
        source, dict | list)

    if setable is False:
        raise ValueError('source')


    if delim in path:
        return _setpath(
            source, path,
            value, delim)


    if isinstance(source, list):

        length = len(source)
        index = int(path)

        if index > length:
            raise IndexError(index)

        if length == index:
            source.append(value)

        elif length > index:
            source[index] = value


    if isinstance(source, dict):
        source[path] = value
