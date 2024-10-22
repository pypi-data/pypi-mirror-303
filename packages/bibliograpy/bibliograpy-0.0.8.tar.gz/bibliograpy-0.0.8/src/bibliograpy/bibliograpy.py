"""
bibliograpy command entrypoint
"""
import logging

from argparse import ArgumentParser, Namespace

from bibliograpy.process import _process

LOG = logging.getLogger(__name__)


def _info(ns: Namespace):
    """info
    """
    LOG.info("info %s", ns)




def _create_parser() -> ArgumentParser:

    # parse argument line
    parser = ArgumentParser(description='Bibliography management.')

    subparsers = parser.add_subparsers(dest='CMD', help='available commands')

    subparsers.add_parser('info', help='get general info')

    process = subparsers.add_parser('process', help='generates bibliograpy source bibliography')
    process.add_argument('file',
                             nargs='?',
                             help="path to the bibliograpy configuration file",
                             default="bibliograpy.yaml")
    process.add_argument('--encoding',
                             nargs='?',
                             help='the bibliograpy configuration file encoding (default to utf-8)',
                             default='utf-8')
    process.add_argument('--output',
                             nargs='?',
                             help='the source bibliograpy file output directory',
                             default='.')
    process.add_argument('--output-file',
                             nargs='?',
                             help='the source bibliograpy output file name',
                             default='bibliography.py')

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'info': _info,
        'process': _process
    }

    ns: Namespace = _create_parser().parse_args()

    commands[ns.CMD](ns)
