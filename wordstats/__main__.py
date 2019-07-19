# -*- coding: utf-8 -*-
"""Tool that prints various statistics on the word list"""

import argparse
import fileinput
import shutil
import sys

from . import __version__

__all__ = ['main']

VERSION = 'wordstats {}'.format(__version__)


def print_histogram(length, lines_number, max_length, max_number, max_width):
    """Prints line length, number of lines of such length, and histogram."""
    lwidth = len(str(max_length))
    nwidth = len(str(max_number))
    max_width = max_width - lwidth - nwidth - 2
    item = {
        'length': length,
        'lwidth': lwidth,
        'num': lines_number,
        'nwidth': nwidth,
        'histogram': '#' * int(max_width * lines_number / max_number),

    }
    print('{length:<{lwidth}} {num:<{nwidth}} {histogram}'.format(**item))


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    parser.add_argument('files', metavar='FILE', nargs='*',
                        help='file that contains word list')

    args = parser.parse_args()
    files = args.files if args.files else ('-',)

    lengths = dict()
    for line in fileinput.input(files=files):
        line_length = len(line.strip())
        lengths[line_length] = lengths.get(line_length, 0) + 1
    min_length = min(lengths.keys())
    max_length = max(lengths.keys())
    max_number = max(lengths.values())
    term_size = shutil.get_terminal_size((80, 24))
    max_width = term_size.columns
    for length in range(min_length, max_length + 1):
        num = lengths.get(length, 0)
        print_histogram(length, num, max_length, max_number, max_width)


if __name__ == "__main__":
    sys.exit(main())
