#!/usr/bin/env python3

import argparse as a
from itertools import cycle

class ConvertCase:
    # def __init__(self, conversions):
    #     self.conversions = conversions

    def uppercase(s):
        return s.upper()

    def lowercase(s):
        return s.lower()

    def titlecase(s):
        return s.title()

    def capitalize(s):
        return s.capitalize()

    def alternating_case(s):
        """
        Given a string, s, returns the string with aLtErNaTiNg cAsE
        """
        case_function = cycle([str.lower, str.upper])
        return ''.join(func(character) for character, func in zip(s, case_function))

    def arg_parse(self):
        p = a.ArgumentParser(description='Change the case of a word or sentence.\nWrap sentences with single quotes.')
        p.add_argument('string', type=str,
                    help='A string to be converted')
        p.add_argument('--convert', '--con', choices=conversions,
                    help='Convert the case of the string. Allowed options are: ' + ', '.join(conversions), metavar='')
        return p.parse_args()

    def convert(self):
        args = ConvertCase.arg_parse(conversions)

        if 'upper' in args.convert:
            print(ConvertCase.uppercase(args.string))

        elif 'lower' in args.convert:
            print(ConvertCase.lowercase(args.string))

        elif 'title' in args.convert:
            print(ConvertCase.titlecase(args.string))

        elif 'sentence' in args.convert:
            print(ConvertCase.capitalize(args.string))

        elif 'sarcastic' in args.convert:
            print(ConvertCase.alternating_case(args.string))

        elif 'all' in args.convert:
            print(*conversions, sep='\n')

        # # Add conversions to conversion list
        # conversion = [uppercase,
        #             lowercase,
        #             title,
        #             sentence,
        #             sarcastic]

if __name__ == "__main__":
    conversions = ['upper', 'lower', 'title', 'sentence', 'sarcastic', 'all']
    ConvertCase.convert(conversions)
