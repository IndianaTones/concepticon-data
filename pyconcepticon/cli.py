# coding: utf8
"""
Main command line interface of the pyconcepticon package.

Like programs such as git, this cli splits its functionality into sub-commands
(see e.g. https://docs.python.org/2/library/argparse.html#sub-commands).
The rationale behind this is that while a lot of different tasks may be triggered using
this cli, most of them require common configuration.

The basic invocation looks like

    concepticon [OPTIONS] <command> [args]

"""
from __future__ import unicode_literals
import sys

from clldutils.clilib import ArgumentParser
from clldutils.path import Path

from pyconcepticon.commands import (link, stats, attributes, intersection, 
        union, map_concepts)
import pyconcepticon

def main():  # pragma: no cover
    parser = ArgumentParser(__name__, link, stats, attributes, intersection,
            union, map_concepts)
    parser.add_argument(
        '--data',
        help="path to concepticon-data",
        default=Path(pyconcepticon.__file__).parent.parent)
    parser.add_argument(
            '--map_type',
            help="type of concept mapping",
            default=1,
            type=int)
    parser.add_argument(
            '--output',
            help="specify output file",
            default=None
            )
    parser.add_argument(
            '--similarity',
            help="specify level of similarity for concept mapping",
            default=5,
            type=int)
    sys.exit(parser.main())
