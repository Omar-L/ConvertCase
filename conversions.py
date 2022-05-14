from itertools import cycle

class Conversions:
    list_of_conversions = ['upper', 'lower', 'title', 'sentence', 'sarcastic', 'all']

    def __init__(self):
        pass

    def uppercase(self, input):
        print(input.upper())

    def lowercase(self, input):
        print(input.lower())

    def titlecase(self, input):
        print(input.title())

    def capitalcase(self, input):
        print(input.capitalize())

    def alternating_case(self, input):
        """
        Given a string, input, returns the string with aLtErNaTiNg cAsE
        """
        case_function = cycle([str.lower, str.upper])
        print(''.join(func(character) for character, func in zip(input, case_function)))
