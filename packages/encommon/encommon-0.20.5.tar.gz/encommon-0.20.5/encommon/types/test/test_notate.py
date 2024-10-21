"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy

from _pytest.python_api import RaisesContext

from pytest import raises

from . import _DICT1R
from ..notate import delate
from ..notate import getate
from ..notate import setate



def test_getate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    value = getate(['1', 2], '1')
    assert value == 2

    value = getate((1, 2), '1')
    assert value == 2

    value = getate({'1': 2}, '1')
    assert value == 2


    path = 'recurse/dict/key'
    value = getate(source, path)

    assert value == 'd1dict'


    path = 'recurse/list/0'
    value = getate(source, path)

    assert value == 'd1list'



def test_getate_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    assert not getate({}, 'd/n/e')
    assert not getate([], '0/n/e')


    path = 'recurse/str/a'
    value = getate(source, path)

    assert value is None



def test_setate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    path = 'list/1'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before is None


    path = 'recurse/dict/key'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1dict'


    path = 'nested/0/dict/key'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1dict'


    path = 'recurse/list/0'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before == 'd1list'



def test_setate_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    path = 'nested/1/dict/key'
    before = getate(source, path)
    setate(source, path, 1)
    after = getate(source, path)
    assert after == 1
    assert before is None



def test_setate_raises() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    _raises: RaisesContext[
        ValueError | IndexError]


    _raises = raises(ValueError)

    with _raises as reason:
        setate(1, '1', 1)  # type: ignore

    _reason = str(reason.value)

    assert _reason == 'source'


    _raises = raises(IndexError)

    with _raises as reason:
        setate([], '1', 1)

    _reason = str(reason.value)

    assert _reason == '1'



def test_delate() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    source = deepcopy(_DICT1R)


    path = 'recurse/dict/key'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1dict'


    path = 'nested/0/dict/key'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1dict'


    path = 'recurse/list/0'
    before = getate(source, path)
    delate(source, path)
    after = getate(source, path)
    assert after is None
    assert before == 'd1list'



def test_delate_raises() -> None:
    """
    Perform various tests associated with relevant routines.
    """


    _raises = raises(ValueError)

    with _raises as reason:
        delate(1, '1')  # type: ignore

    _reason = str(reason.value)

    assert _reason == 'source'


    _raises = raises(ValueError)

    with _raises as reason:
        delate({'a': 1}, 'a/1/c')

    _reason = str(reason.value)

    assert _reason == 'source'
