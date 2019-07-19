# -*- coding: utf-8 -*-
"""Tool that prints various statistics on the word list"""

import argparse
import sys

__all__ = ['main']


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
