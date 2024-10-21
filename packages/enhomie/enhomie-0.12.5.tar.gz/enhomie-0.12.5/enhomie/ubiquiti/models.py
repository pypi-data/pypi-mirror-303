"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING
from typing import Type

if TYPE_CHECKING:
    from .params import DriverUbiqClientParams
    from .params import UbiqOriginParams
    from .update import UbiqUpdateItem



class UbiqDriverModels:
    """
    Return the class object that was imported within method.
    """


    @classmethod
    def client(
        cls,
    ) -> Type['DriverUbiqClientParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            DriverUbiqClientParams)

        return DriverUbiqClientParams



class UbiqModels:
    """
    Return the class object that was imported within method.
    """


    @classmethod
    def origin(
        cls,
    ) -> Type['UbiqOriginParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            UbiqOriginParams)

        return UbiqOriginParams


    @classmethod
    def update(
        cls,
    ) -> Type['UbiqUpdateItem']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .update import (
            UbiqUpdateItem)

        return UbiqUpdateItem


    @classmethod
    def drivers(
        cls,
    ) -> Type['UbiqDriverModels']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        return UbiqDriverModels
