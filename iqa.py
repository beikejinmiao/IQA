#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import argparse
from mode import IQAMode


class IQAMain(object):

    _usage_example = """Examples of use:
$ python iqa.py --mode=test
"""

    def __init__(self):
        self.args = self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser(epilog=self._usage_example)
        # run mode
        parser.add_argument("-m", "--mode",
                            choices=["train", "test", "server"], default="test", help="Run mode")

        args = parser.parse_args()
        return args


def main():
    iqa = IQAMain()
    mode = iqa.args.mode
    runtime = getattr(IQAMode(mode), mode)
    runtime()
    return 0


if __name__ == '__main__':
    sys.exit(main())

