import argparse as a
from itertools import cycle


def alternating_case(s):
    """
    Given a string, s, returns the string with aLtErNaTiNg cAsE
    """
    case_function = cycle([str.lower, str.upper])
    return ''.join(func(character) for character, func in zip(s, case_function))


def arg_parse():
    conversions = ['upper', 'lower', 'title', 'sentence', 'sarcastic', 'all']

    p = a.ArgumentParser(description='Change the case of a word or sentence.\nWrap sentences with single quotes.')
    p.add_argument('string', type=str,
                   help='A string to be converted')
    p.add_argument('--convert', '--con', choices=conversions,
                   help='Convert the case of the string. Allowed options are: ' + ', '.join(conversions), metavar='')
    return p.parse_args()


def main():
    args = arg_parse()

    # Case conversion for the string
    uppercase = args.string.upper()
    lowercase = args.string.lower()
    title = args.string.title()
    sentence = args.string.capitalize()
    sarcastic = alternating_case(args.string)
    # Add conversions to conversion list
    conversion = [uppercase,
                  lowercase,
                  title,
                  sentence,
                  sarcastic]

    # Uppercase
    if args.convert == 'upper':
        print(conversion[0])
    # Lowercase
    elif args.convert == 'lower':
        print(conversion[1])
    # Title
    elif args.convert == 'title':
        print(conversion[2])
    # Sentence
    elif args.convert == 'sentence':
        print(conversion[3])
    # Sarcastic
    elif args.convert == 'sarcastic':
        print(conversion[4])
    # All conversions
    elif args.convert == 'all':
        print(*conversion, sep='\n')


if __name__ == "__main__":
    main()
