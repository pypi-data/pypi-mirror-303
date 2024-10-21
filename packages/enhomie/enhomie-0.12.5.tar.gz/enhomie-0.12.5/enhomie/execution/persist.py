"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from argparse import ArgumentParser
from sys import argv as sys_argv
from typing import Optional

from encommon.types import DictStrAny

from ..homie import Homie
from ..homie import HomieConfig



def arguments(
    args: Optional[list[str]] = None,
) -> DictStrAny:
    """
    Construct arguments which are associated with the file.

    :param args: Override the source for the main arguments.
    :returns: Construct arguments from command line options.
    """

    parser = ArgumentParser()

    args = args or sys_argv[1:]


    parser.add_argument(
        '--config',
        required=True,
        help=(
            'complete or relative '
            'path to config file'))


    parser.add_argument(
        '--console',
        action='store_true',
        default=False,
        help=(
            'write log messages '
            'to standard output'))


    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help=(
            'increase logging level '
            'for standard output'))


    parser.add_argument(
        '--unique',
        required=True,
        help=(
            'unique identifier to '
            'store provided value'))


    parser.add_argument(
        '--value',
        help=(
            'value stored at the '
            'provided unique key'))


    parser.add_argument(
        '--expire',
        default='30m',
        help=(
            'after when value will '
            'be removed from table'))


    return vars(
        parser
        .parse_args(args))



def operation(
    # NOCVR
    homie: Homie,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param homie: Primary class instance for Homie Automate.
    """

    config = homie.config
    sargs = config.sargs

    unique = sargs['unique']
    value = sargs['value']
    expire = sargs['expire']

    (homie.persist
     .insert(unique, value, expire))


def execution(
    # NOCVR
    args: Optional[list[str]] = None,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param args: Override the source for the main arguments.
    """

    config = HomieConfig(
        arguments(args))

    config.logger.start()

    config.logger.log_i(
        base='execution/persist',
        status='started')

    homie = Homie(config)

    operation(homie)

    config.logger.log_i(
        base='execution/persist',
        status='stopped')

    config.logger.stop()



if __name__ == '__main__':
    execution()  # NOCVR
