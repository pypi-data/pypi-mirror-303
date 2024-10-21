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



def test_HomieChilds(
    homie: 'Homie',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param homie: Primary class instance for Homie Automate.
    """

    childs = homie.childs


    attrs = lattrs(childs)

    assert attrs == [
        '_HomieChilds__homie',
        '_HomieChilds__origins',
        '_HomieChilds__devices',
        '_HomieChilds__groups',
        '_HomieChilds__scenes',
        '_HomieChilds__desires',
        '_HomieChilds__aspires']


    assert inrepr(
        'homie.HomieChilds',
        childs)

    assert isinstance(
        hash(childs), int)

    assert instr(
        'homie.HomieChilds',
        childs)


    childs.validate()

    assert childs.origins

    assert childs.devices

    assert childs.groups

    assert childs.scenes

    assert childs.desires

    assert childs.aspires
