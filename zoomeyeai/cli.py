#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
* Filename: cli.py
* Description: cli program entry
* Time: 2024.12.05
*/
"""

import argparse
import os
import sys

module_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(1, module_path)

from zoomeyeai import core
from zoomeyeai.config import BANNER


def get_version():
    print(BANNER)


class ZoomEyeParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        sys.exit(2)


def main():
    """
    parse user input args
    :return:
    """

    parser = ZoomEyeParser(prog='zoomeye')
    subparsers = parser.add_subparsers()
    # show ZoomEye-python version number
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="show program's version number and exit"
    )

    # initial account configuration related commands

    P_init = subparsers.add_parser("init", help="Initialize the token for ZoomEye-python.")
    P_init.add_argument("-apikey", help="ZoomEye API Key", default=None, metavar='[api key]')
    P_init.set_defaults(func=core.init)

    # zoomeye account info
    parser_info = subparsers.add_parser("info", help="Show ZoomEye account info")
    parser_info.set_defaults(func=core.info)

    """
    version:2.3.0
    change_log:
        update search
    """
    search_v2_parser = subparsers.add_parser("search",
                                             help="get network asset information based on query conditions.")
    search_v2_parser.add_argument("dork", type=str, help="search key word(eg=baidu.com)", default=None)

    search_v2_parser.add_argument(
        "-facets",
        default='',
        type=str,
        help=('''
              if this parameter is specified,
                     the corresponding data will be displayed
                     at the end of the returned result.
                     supported : 'product', 'device', 'service', 'os', 'port', 'country', 'subdivisions', 'city'
          '''),
        metavar='facets'
    )
    search_v2_parser.add_argument(
        "-fields",
        default='',
        metavar='field=regexp',
        type=str,
        help=('''
               display data based on input fields
               please see: https://www.zoomeye.ai/doc/
          ''')
    )
    search_v2_parser.add_argument("-sub_type", type=str, help="specify the type of data to search",
                                  choices=('v4', 'v6', 'web', 'all'), default='all')
    search_v2_parser.add_argument("-page", metavar='page', type=int, help="view the page of the query result",
                                  default=1)
    search_v2_parser.add_argument('-pagesize', metavar='pagesize', type=int,
                                  help="specify the number of pagesize to search", default=20)
    search_v2_parser.add_argument(
        "-figure",
        help="Pie chart or bar chart showing data，can only be used under facet and stat",
        choices=('pie', 'hist'),
        default=None
    )
    search_v2_parser.set_defaults(func=core.search)

    args = parser.parse_args()
    ver = args.version

    if ver:
        get_version()
        exit(0)

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()


if __name__ == '__main__':
    main()
