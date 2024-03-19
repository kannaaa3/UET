"""
Import Regex library.
"""
import re
from helper import bcolors


class Token():
    _type = 'Unknown'
    lexeme = None

    def __init__(self, _type, lexeme) -> None:
        self._type = _type
        self.lexeme = lexeme

    def __str__(self) -> str:
        return f"({self._type}, '{self.lexeme}')"


class Scanner():

    DELIMITERS = "();><=+*/"

    # (regex, name) of tokens
    TOKEN_REGEX = [
        # NOTE:
        # Keyword higher priority
        ('^if$', "IF"),
        ('^then$', "THEN"),
        ('^else$', 'ELSE'),
        ('^int$', "INTEGER"),
        ('^bool$', "BOOLEAN"),

        ('^true$|^false$', "BOOLEAN CONSTANT"),
        ("^[0]|[1-9][0-9]*$", 'INTEGER CONSTANT'),

        # NOTE:
        # Lower priority
        ("^[a-z]+[0-9]*$", "IDENTIFIER"),
        ("^[=]$", "ASSIGN"),
        ("^>$|^>=$|^==$", 'ROP'),
        ('^[;]$', 'SEMI'),
        ('^[(]$', 'L_PARENTHESES'),
        ('^[)]$', 'R_PARENTHESES'),
        ('^[{]$', "L_BRACKET"),
        ('^[}]$', "R_BRACKET"),
        ('^\\+$', "ADD"),
        ('^\\*$', "MUL"),

        ("^//[.]*$", bcolors.violet("1-LINE COMMENT")),
        ("^/\\*[.]*\\*/$", bcolors.green("MULTILINE COMMENT")),

    ]

    # OP = '[*/+-]'
    # TYPE = ['float', 'int']

    def __init__(self) -> None:
        pass

    def getTokenForm(self, content):
        _type = f'{bcolors.CRED}Unknown{bcolors.CEND}'

        for tp in self.TOKEN_REGEX:
            if re.match(tp[0], content):
                _type = tp[1]
                break

        return Token(_type, content)

    def normalize(self, content):
        def check_need_space(x, y):
            return (x in self.DELIMITERS and y not in self.DELIMITERS) \
                or (x not in self.DELIMITERS and y in self.DELIMITERS) \
                or (y == ";")

        chars = []

        for i in range(len(content)-1):
            chars.append(content[i])
            if check_need_space(content[i], content[i+1]):
                chars.append(' ')

        chars.append(content[-1])

        return "".join(chars)

    def scan(self, content):
        """
        Scan the content and return a list of tokens.
        """
        res = []
        content = self.normalize(content)
        words = content.split(' ')

        for word in words:
            print("Current word:", word)
            res.append(self.getTokenForm(word))

        return res


def main():
    with open("inp.upl", "r") as f:
        content = f.read()

    scanner = Scanner()
    tokens = scanner.scan(content)
    for x in tokens:
        print(x)


if __name__ == "__main__":
    main()
