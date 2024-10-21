"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any

from encommon.times import unitime

from pydantic import Field

from .common import HomieParamsModel
from ..addons import HomiePersistExpire
from ..addons import HomiePersistValue



class HomieStoreParams(HomieParamsModel, extra='forbid'):
    """
    Process and validate the Homie configuration parameters.
    """

    unique: Annotated[
        str,
        Field(...,
              description='Unique key for the value',
              min_length=1)]

    value: Annotated[
        HomiePersistValue,
        Field(...,
              description='Value stored at the key')]

    expire: Annotated[
        HomiePersistExpire,
        Field('1d',
              description='After when the key expires')]


    def __init__(
        # NOCVR
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        expire = data.get('expire')

        if isinstance(expire, str):
            expire = unitime(expire)
            assert expire >= 0

        super().__init__(**data)
