#!/usr/bin/env python3

import argparse as a
from conversions import Conversions as c

def arg_parse():
    conversions = c.list_of_conversions
    p = a.ArgumentParser(description='Change the case of a word or sentence.\nWrap sentences with single quotes, or double quotes if you have apostrophes in the string.')   # type: ignore
    p.add_argument('string', type=str, 
                    help='A string to be converted')
    p.add_argument('--convert', '--con', choices=conversions, required=True,
                    help='Convert the case of the string. Allowed options are: ' + ', '.join(conversions), metavar='')

    return p.parse_args()


def convert():
    args = arg_parse()

    if 'upper' in args.convert:
        print(c.upper_case(args.string))

    elif 'lower' in args.convert:
        print(c.lower_case(args.string))

    elif 'title' in args.convert:
        print(c.title_case(args.string))

    elif 'sentence' in args.convert:
        print(c.capital_case(args.string))

    elif 'sarcastic' in args.convert:
        print(c.alternating_case(args.string))

    else:
        print(*c.all(args.string), sep='\n')


if __name__ == "__main__":
    convert()
