import argparse as a


def arg_parse():
    p = a.ArgumentParser(description='Change the case of a word or sentence.\nWrap sentences with single quotes.')
    p.add_argument('string', type=str,
                   help='A string to be converted')
    p.add_argument('--up', "--upper", action="store_true",
                   help='Capitalize all letters in the string.')
    p.add_argument('--low', "--lower", action="store_true",
                   help='Lowercase all letters in the string.')
    p.add_argument('--tit', "--title", action="store_true",
                   help='Titlecase all letters in the string.')
    p.add_argument('--sen', "--sentence", action="store_true",
                   help='Sentencecase all letters in the string.')
    p.add_argument('--a', "--all", action="store_true",
                   help='Provide all conversions for the string.')
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
    if args.up:
        print(conversion[0])
    # Lowercase
    elif args.low:
        print(conversion[1])
    # Title
    elif args.tit:
        print(conversion[2])
    # Sentence
    elif args.sen:
        print(conversion[3])
    # All conversions
    elif args.a:
        print(*conversion, sep='\n')


if __name__ == "__main__":
    main()
