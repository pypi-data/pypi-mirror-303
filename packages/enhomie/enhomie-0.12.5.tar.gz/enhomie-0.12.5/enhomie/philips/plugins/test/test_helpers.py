"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from ..helpers import phue_changed
from ..helpers import phue_sensors
from ...origin import PhueOrigin
from ....utils.tests import STARTED

if TYPE_CHECKING:
    from ....homie import Homie
    from ....utils import TestBodies



def test_phue_changed(
    homie: 'Homie',
    bodies: 'TestBodies',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param homie: Primary class instance for Homie Automate.
    :param bodies: Locations and groups for use in testing.
    """

    childs = homie.childs
    origins = childs.origins
    devices = childs.devices


    planets = bodies.planets

    for planet in planets:

        origin = origins[
            f'{planet}_philips']

        device = devices[
            f'{planet}_button']

        assert isinstance(
            origin, PhueOrigin)

        assert origin.refresh()


        timestamp = (
            STARTED
            .shift('-1d@h'))


        assert device.source

        changed = phue_changed(
            device.source)

        assert changed == {
            'button1': None,
            'button2': timestamp,
            'button3': timestamp,
            'button4': None}



def test_phue_sensors(
    homie: 'Homie',
    bodies: 'TestBodies',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param homie: Primary class instance for Homie Automate.
    :param bodies: Locations and groups for use in testing.
    """

    childs = homie.childs
    origins = childs.origins
    devices = childs.devices


    planets = bodies.planets

    for planet in planets:

        origin = origins[
            f'{planet}_philips']

        device = devices[
            f'{planet}_motion']

        assert isinstance(
            origin, PhueOrigin)

        assert origin.refresh()


        assert device.source

        sensors = phue_sensors(
            device.source)

        prefix = (
            'aa012345'
            if planet == 'jupiter'
            else 'bb012345')

        motion = (
            f'{prefix}-abcd-1234'
            '-ab12-abcdef000025')

        assert sensors == {
            'motion': motion}
