"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from re import match as re_match

from .parse import since_time



def unitime(
    input: int | float | str,
) -> int:
    """
    Return the seconds in integer format for provided input.

    Example
    -------
    >>> unitime('1d')
    86400
    >>> unitime('1y')
    31536000
    >>> unitime('1w3d4h')
    878400

    :param input: Input that will be converted into seconds.
    :returns: Seconds in integer format for provided input.
    """

    notate = r'^(\d+(s|m|h|d|w|y))*$'
    strint = r'^\d+$'
    strflt = r'^\d+\.\d+$'

    if isinstance(input, str):

        if re_match(notate, input):
            input = since_time(
                'now', f'+{input}')

        elif re_match(strint, input):
            input = int(input)

        elif re_match(strflt, input):
            input = int(
                input.split('.')[0])

    if isinstance(input, float):
        input = int(input)

    assert isinstance(input, int)

    return input
