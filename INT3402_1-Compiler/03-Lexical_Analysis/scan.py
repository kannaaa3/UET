"""
Import Regex library.
"""
import re


class Token():
    _type = 'Unknown'
    lexeme = None

    def __init__(self, _type, lexeme) -> None:
        self._type = _type
        self.lexeme = lexeme

    def __str__(self) -> str:
        return f"({self._type}, {self.lexeme})"


class Scanner():

    KEYWORD = ['if', 'then', 'else']

    SPECIAL_CHARS = "();><="

    # (regex, name) of tokens
    TOKEN_REGEX = [
        ("^[a-z][0-9][a-z0-9]*$", 'IDENTIFIER'),
        ("^[0]|[1-9][0-9]*$", 'NUMBER'),
        ("^[=]$", "ASSIGN"),
        ("^[<>]$", 'ROP'),
        ('^[;]$', 'SEMI')
    ]

    # OP = '[*/+-]'
    # TYPE = ['float', 'int']

    def __init__(self) -> None:
        pass

    def getTokenForm(self, content):
        _type = 'Unknown'

        if content in self.KEYWORD:
            _type = 'KEYWORD'
        else:
            for tp in self.TOKEN_REGEX:
                if re.match(tp[0], content):
                    _type = tp[1]
                    break

        return Token(_type, content)

    def normalize(self, content):
        def check_need_space(x, y):
            return (x in self.SPECIAL_CHARS and y not in self.SPECIAL_CHARS) \
                or (x not in self.SPECIAL_CHARS and y in self.SPECIAL_CHARS) \
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
        words = content.split()

        for word in words:
            res.append(self.getTokenForm(word))

        return res


def main():
    print("Enter filename: ")
    with open(input(), "r") as f:
        content = f.read()

    scanner = Scanner()
    tokens = scanner.scan(content)
    for x in tokens:
        print(x)


if __name__ == "__main__":
    main()
