# ozi/fix/parser.py
# Part of the OZI Project, under the Apache License v2.0 with LLVM Exceptions.
# See LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""``ozi-fix`` console application."""
import sys
from argparse import SUPPRESS
from argparse import ArgumentParser
from argparse import BooleanOptionalAction

from ozi_core._i18n import TRANSLATION
from ozi_core.new.defaults import COPYRIGHT_HEAD

parser = ArgumentParser(
    prog='ozi-fix',
    description=sys.modules[__name__].__doc__,
    add_help=False,
    usage=f"""%(prog)s [{TRANSLATION('term-options')}] | [{TRANSLATION('term-positional-args')}]

{TRANSLATION('adm-disclaimer-text')}
""",
)
parser.add_argument(
    '--add',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=SUPPRESS,
)
parser.add_argument(
    '--remove',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=SUPPRESS,
)
parser.add_argument(
    '--strict',
    default=False,
    action=BooleanOptionalAction,
    help=SUPPRESS,
)
parser.add_argument(
    '--pretty',
    default=False,
    action=BooleanOptionalAction,
    help=SUPPRESS,
)
subparser = parser.add_subparsers(help='', metavar='', dest='fix')
helpers = parser.add_mutually_exclusive_group()
helpers.add_argument('-h', '--help', action='help', help=TRANSLATION('term-help-help'))
missing_parser = subparser.add_parser(
    'missing',
    prog='ozi-fix missing',
    aliases=['m', 'mis'],
    usage=f'%(prog)s [{TRANSLATION("term-options")}] [{TRANSLATION("term-output")}] target',
    allow_abbrev=True,
    help=TRANSLATION('term-help-fix-missing'),
)
missing_parser.add_argument(
    '--add',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=SUPPRESS,
)
missing_parser.add_argument(
    '--remove',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=SUPPRESS,
)
missing_output = missing_parser.add_argument_group(TRANSLATION('term-output'))
missing_output.add_argument(
    '--strict',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-strict'),
)
missing_output.add_argument(
    '--pretty',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-pretty'),
)
missing_parser.add_argument(
    'target',
    type=str,
    nargs='?',
    default='.',
    help=TRANSLATION('term-help-fix-target'),
)
source_parser = subparser.add_parser(
    'source',
    aliases=['s', 'src'],
    prog='ozi-fix source',
    usage=f'%(prog)s [{TRANSLATION("term-options")}] [{TRANSLATION("term-output")}] target',
    allow_abbrev=True,
    help=TRANSLATION('term-help-fix-source'),
)
test_parser = subparser.add_parser(
    'test',
    prog='ozi-fix test',
    usage=f'%(prog)s [{TRANSLATION("term-options")}] [{TRANSLATION("term-output")}] target',
    aliases=['t', 'tests'],
    allow_abbrev=True,
    help=TRANSLATION('term-help-fix-test'),
)
source_parser.add_argument(
    '-a',
    '--add',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=TRANSLATION('term-help-fix-add'),
)
source_parser.add_argument(
    '-r',
    '--remove',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=TRANSLATION('term-help-fix-remove'),
)
source_parser.add_argument(
    '-c',
    '--copyright-head',
    metavar='HEADER',
    type=str,
    default=COPYRIGHT_HEAD,
    help=TRANSLATION('term-copyright-head'),
)
source_output = source_parser.add_argument_group(TRANSLATION('term-output'))
source_output.add_argument(
    '--strict',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-strict'),
)
source_output.add_argument(
    '--pretty',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-pretty'),
)
source_parser.add_argument(
    'target',
    type=str,
    nargs='?',
    default='.',
    help=TRANSLATION('term-help-fix-target'),
)
test_parser.add_argument(
    '-a',
    '--add',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=TRANSLATION('term-help-fix-add'),
)
test_parser.add_argument(
    '-r',
    '--remove',
    metavar='FILENAME',
    nargs='?',
    action='append',
    default=['ozi.phony'],
    help=TRANSLATION('term-help-fix-remove'),
)
test_parser.add_argument(
    '-c',
    '--copyright-head',
    metavar='HEADER',
    type=str,
    default=COPYRIGHT_HEAD,
    help=TRANSLATION('term-copyright-head'),
)
test_output = test_parser.add_argument_group(TRANSLATION('term-output'))
test_output.add_argument(
    '--strict',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-strict'),
)
test_output.add_argument(
    '--pretty',
    default=False,
    action=BooleanOptionalAction,
    help=TRANSLATION('term-help-pretty'),
)
test_parser.add_argument(
    'target',
    type=str,
    nargs='?',
    default='.',
    help=TRANSLATION('term-help-fix-target'),
)
