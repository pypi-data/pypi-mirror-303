"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional
from typing import TYPE_CHECKING

from encommon.times import Time
from encommon.types import getate
from encommon.types import sort_dict

if TYPE_CHECKING:
    from ..helpers import PhueFetch



_CHANGED = dict[str, Optional[Time]]

_SENSORS = dict[str, str]

_REPORTS = ['button', 'contact', 'motion']



def phue_changed(
    source: 'PhueFetch',
) -> _CHANGED:
    """
    Return the timestamp for the services that have changed.

    :param source: Content which will be shown after header.
    :returns: Timestamp for the services that have changed.
    """

    changed: _CHANGED = {}


    services = (
        source['services'])


    for item in services:

        rtype = item['rtype']

        if rtype not in _REPORTS:
            continue

        fetch = item['_source']


        base = f'{rtype}_report'
        key = 'changed'

        if rtype == 'button':
            key = 'updated'


        time = getate(
            (fetch[rtype]
             if rtype != 'contact'
             else fetch),
            f'{base}/{key}')


        index = getate(
            fetch,
            'metadata/control_id')

        if index is not None:
            rtype += str(index)

        changed[rtype] = (
            Time(time)
            if time is not None
            else None)


    return sort_dict(changed)



def phue_sensors(
    source: 'PhueFetch',
) -> _SENSORS:
    """
    Return the unique identifier for services on the device.

    :param source: Content which will be shown after header.
    :returns: Timestamp for the services that have changed.
    """

    sensors: _SENSORS = {}


    services = (
        source['services'])


    for item in services:

        rtype = item['rtype']
        rid = item['rid']

        if rtype not in _REPORTS:
            continue

        fetch = item['_source']

        index = getate(
            fetch,
            'metadata/control_id')

        if index is not None:
            rtype += str(index)

        sensors[rtype] = rid


    return sort_dict(sensors)
