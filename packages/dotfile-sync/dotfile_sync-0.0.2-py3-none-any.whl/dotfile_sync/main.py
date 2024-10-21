#!/usr/bin/env python3
import argparse

from . import helper, subparser

parser = argparse.ArgumentParser(description='dotfile-manager')
parser.add_argument('-v', '--version', action='version', version=helper.get_version())
subparsers = parser.add_subparsers()
subparser.add_sync_parser(
    subparsers.add_parser('sync', help='Sync dotfiles', aliases=['s'])
)


def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
