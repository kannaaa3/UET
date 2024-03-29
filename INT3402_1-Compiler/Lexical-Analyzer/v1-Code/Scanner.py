#!/bin/python
import sys

"""
Regex library.
"""
import re
from enum import IntEnum, auto

class TokenType(IntEnum):
    """
    Note that the priority of reserved words is higher.
    """
    DO = auto()
    WHILE = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    PRINT = auto()

    INT_T = auto()
    BOOL_T = auto()

    BEGIN = auto()
    END = auto()

    CONST_BOOL = auto()
    CONST_INT = auto()

    ADD = auto()
    MUL = auto()

    IDENTIFIER = auto()

    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()

    ROP = auto()
    ASSIGN = auto()
    SEMICOLON = auto()
    UNKNOWN = auto()
    EOF = auto()


class Token():
    """
    Storing Token value and position (for error detection).
    """
    def __init__(self, token_t: TokenType, lexeme: str, col: int, row: int) -> None:
        self.token_t = token_t
        self.lexeme = lexeme
        self.col = col
        self.row = row

    def __str__(self) -> str:
        return f"(<{self.token_t._name_}>, {self.lexeme})"


class Scanner():
    rb = lambda s: r'{}\b'.format(s)

    regex = dict()
    regex[TokenType.DO] = rb("do")
    regex[TokenType.WHILE] = rb("while")
    regex[TokenType.IF] = rb("if")
    regex[TokenType.THEN] = rb("then")
    regex[TokenType.ELSE] = rb("else")
    regex[TokenType.PRINT] = rb("print")

    regex[TokenType.INT_T] = rb("int")
    regex[TokenType.BOOL_T] = rb("bool")

    regex[TokenType.BEGIN] = rb("begin")
    regex[TokenType.END] = rb("end")

    regex[TokenType.CONST_BOOL] = rb("(true|false)")
    regex[TokenType.CONST_INT] = r"[0]\b|[1-9][0-9]*"

    regex[TokenType.ADD] = r"[+]"
    regex[TokenType.MUL] = r"[*]"

    regex[TokenType.LEFT_BRACKET] = r"[(]"
    regex[TokenType.RIGHT_BRACKET] = r"[)]"
    regex[TokenType.LEFT_PARENTHESIS] = r"{"
    regex[TokenType.RIGHT_PARENTHESIS] = r"}"

    regex[TokenType.IDENTIFIER] = r"[a-z]+[0-9]*\b"

    regex[TokenType.ROP] = r"==|<=|>=|<|>"
    regex[TokenType.ASSIGN] = r"[=]"
    regex[TokenType.SEMICOLON] = r"[;]"
    regex[TokenType.UNKNOWN] = r"."

    OPEN_CMT = r"/[*]"
    CLOSE_CMT = r"[*]/"
    OPEN_1L_CMT = r"//"

    # variables
    buffer = ""
    lexemeBegin = 0
    file_path = ""
    f = open("inp")
    

    def __init__(self) -> None:
        pass

    def scan(self, path: str) -> None:

        if self.file_path is not None:
            self.f.close()

        self.file_path = path
        self.f = open(self.file_path)
        self.is_done = False
        self.row = 0
        self.next_line()

    def next_line(self) -> None:
        """
        Update the current buffer to the next line of the source.
        Move the lexemeBegin ptr to the first character that is neither spc nor \t.
        """
        self.buffer = self.f.readline()

        if len(self.buffer) == 0:
            self.is_done = True
            return

        self.buffer = self.buffer[:-1]
        self.buffer_len = len(self.buffer)

        self.row += 1
        self.lexemeBegin = 0
        self.ignore_spc()

    def reach_end_of_line(self):
        return self.lexemeBegin == self.buffer_len

    def nextToken(self) -> Token:
        """
        Return the next token.
        """

        while self.reach_end_of_line() and not self.is_done:
            self.next_line()

        current_buf = self.buffer[self.lexemeBegin:]

        # If 1 line comment: move to the next line
        if re.match(self.OPEN_1L_CMT, current_buf):
            self.next_line()
            return self.nextToken()

        if self.is_done:
            return Token(TokenType.EOF, "", 0, self.row)

        # If multiline comment
        if re.match(self.OPEN_CMT, current_buf):
            row = self.row
            col = self.lexemeBegin
            # keep parsing until encounter comment closed
            while True:
                res = re.search(self.CLOSE_CMT, self.buffer[self.lexemeBegin:])
                if res is not None:
                    r = res.span()[1]
                    self.lexemeBegin = r
                    self.ignore_spc()
                    current_buf = self.buffer[self.lexemeBegin:]
                    break

                self.next_line()

                if self.is_done:
                    raise Exception(f"Multiline comment not closed at row {row}, col {col}!")

        # get token
        for t in TokenType:
            res = re.match(self.regex[t], self.buffer[self.lexemeBegin:])
            if res is not None:
                l, r = res.span()
                l += self.lexemeBegin
                r += self.lexemeBegin
                lexeme = self.buffer[l:r]
                self.lexemeBegin = r
                self.ignore_spc()
                return Token(t, lexeme, l, self.row)


    def ignore_spc(self):
        """
        Skip all spaces and tabs to get to the next token.
        """
        ptr = self.lexemeBegin
        while ptr < self.buffer_len and self.buffer[ptr] in ' \t':
            ptr = ptr + 1
        self.lexemeBegin = ptr

        if self.reach_end_of_line():
            self.next_line()
            if not self.is_done:
                self.ignore_spc()

    def get_buf(self):
        return self.buffer

if __name__ == "__main__":
    scanner = Scanner()
    
    if len(sys.argv) < 2:
        print("Usage: ./Scanner.py file_path")
        exit(0)

    path = sys.argv[1]
    scanner.scan(path)
    while True:
        res = scanner.nextToken()
        if res.token_t == TokenType.EOF:
            break
        if res.token_t == TokenType.UNKNOWN:
            row, col = (res.row, res.col)
            print(f"Unknown token at row: {row}, col: {col}: \"{scanner.get_buf()[col:]}\"")
            exit()
        print(res)
