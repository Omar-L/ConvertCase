import argparse as a


def arg_parse():
    conversions = ['upper', 'lower', 'title', 'sentence', 'all']

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

    # Add conversions to conversion list
    conversion = [uppercase,
                  lowercase,
                  title,
                  sentence]

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
    # All conversions
    elif args.convert == 'all':
        print(*conversion, sep='\n')


if __name__ == "__main__":
    main()
