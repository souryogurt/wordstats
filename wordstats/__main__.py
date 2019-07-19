# -*- coding: utf-8 -*-
"""Tool that prints various statistics on the word list"""

import argparse
import fileinput
import sys

from . import __version__

__all__ = ['main']

VERSION = 'wordstats {}'.format(__version__)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    parser.add_argument('files', metavar='FILE', nargs='*',
                        help='file that contains word list')

    args = parser.parse_args()
    files = args.files if args.files else ('-',)
    for line in fileinput.input(files=files):
        print(line.strip())


if __name__ == "__main__":
    sys.exit(main())
