from itertools import cycle

class Conversions:
    list_of_conversions = ['upper', 'lower', 'title', 'sentence', 'sarcastic', 'all']

    @staticmethod
    def upper_case(s: str) -> str:
        """
        Given a string, s, return the string with <<UPPER CASE>>
        """
        return s.upper()

    @staticmethod   
    def lower_case(s: str) -> str:
        """
        Given a string, s, return the string with <<lower case>>
        """
        return s.lower()
    
    @staticmethod
    def title_case(s: str) -> str:
        """
        Given a string, s, return the string with <<Title Case>>
        """
        return s.title()

    @staticmethod
    def capital_case(s: str) -> str:
        """
        Given a string, s, return the string with <<Capital case>>
        """
        return s.capitalize()

    @staticmethod
    def alternating_case(s: str) -> str:
        """
        Given a string, s, returns the string with aLtErNaTiNg cAsE
        """
        case_function = cycle([str.lower, str.upper])
        return ''.join(func(character) for character, func in zip(s, case_function))

    @staticmethod
    def all(s: str) -> list:
        del Conversions.all
        _list = []
        
        for callable in Conversions.__dict__.values():
            try:
                _list.append(callable(s))
            except TypeError:
                pass
        return _list