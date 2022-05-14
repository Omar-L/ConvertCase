#!/usr/bin/env python3

import argparse as a
from conversions import Conversions

c = Conversions()
conversions = c.list_of_conversions

def arg_parse():
    p = a.ArgumentParser(description='Change the case of a word or sentence.\nWrap sentences with single quotes.')
    p.add_argument('string', type=str,
                help='A string to be converted')
    p.add_argument('--convert', '--con', choices=conversions,
                help='Convert the case of the string. Allowed options are: ' + ', '.join(conversions), metavar='')
    return p.parse_args()

def convert():
    args = c.arg_parse(conversions)

    if 'upper' in args.convert:
        print(c.uppercase(args.string))

    elif 'lower' in args.convert:
        print(c.lowercase(args.string))

    elif 'title' in args.convert:
        print(c.titlecase(args.string))

    elif 'sentence' in args.convert:
        print(c.capitalcase(args.string))

    elif 'sarcastic' in args.convert:
        print(c.alternating_case(args.string))


if __name__ == "__main__":
    convert()
    