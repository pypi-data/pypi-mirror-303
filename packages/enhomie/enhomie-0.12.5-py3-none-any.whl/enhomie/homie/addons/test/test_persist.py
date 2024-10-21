"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs

if TYPE_CHECKING:
    from ...homie import Homie



def test_HomiePersist(
    homie: 'Homie',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param homie: Primary class instance for Homie Automate.
    """

    persist = homie.persist


    attrs = lattrs(persist)

    assert attrs == [
        '_HomiePersist__homie',
        '_HomiePersist__connect',
        '_HomiePersist__locker',
        '_HomiePersist__sengine',
        '_HomiePersist__session']


    assert inrepr(
        'persist.HomiePersist',
        persist)

    assert isinstance(
        hash(persist), int)

    assert instr(
        'persist.HomiePersist',
        persist)


    persist.insert(
        unique='present',
        value=False)

    value = (
        persist
        .select('present'))

    assert value is False


    persist.delete(
        unique='present')

    value = (
        persist
        .select('present'))

    assert value is None


    persist.insert(
        unique='present',
        value=True,
        expire=-1)

    value = (
        persist
        .select('present'))

    assert value is None



def test_HomiePersist_cover(
    homie: 'Homie',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param homie: Primary class instance for Homie Automate.
    """

    persist = homie.persist


    persist.insert(
        unique='present',
        value=None)

    value = (
        persist
        .select('present'))

    assert value is None


    persist.insert(
        unique='types',
        value=1)

    value = (
        persist
        .select('types'))

    assert value == 1


    persist.insert(
        unique='types',
        value=1.0)

    value = (
        persist
        .select('types'))

    assert value == 1.0


    persist.insert(
        unique='types',
        value='string')

    value = (
        persist
        .select('types'))

    assert value == 'string'


    persist.insert(
        unique='types',
        value=True)

    value = (
        persist
        .select('types'))

    assert value is True


    persist.insert(
        unique='types',
        value=None)

    value = (
        persist
        .select('types'))

    assert value is None
