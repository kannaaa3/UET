<h1 align="center"> 🔹 Lexical Analyzer 🔹</h1>
### Our group: 

- 21020055 Trần Thùy Dung 
- 21020037 Nguyễn Đức Thuận 
- 21020455 Lê Quốc Toản


### Run
```
❯ python scan.py
Enter filename: inp.upl
(IDENTIFIER, s1um)         <------ valid variable name
(ASSIGN, =)
(NUMBER, 0)
(KEYWORD, then)
(Unknown, x)
(ASSIGN, =)
(NUMBER, 10)
(KEYWORD, else)
(Unknown, sum)             <------- invalid variable name
(ASSIGN, =)
(NUMBER, 40)
(SEMI, ;)
(KEYWORD, if)
(Unknown, sum)
...
```


#### ________________________________________________________________________________________________




### Problem
Write a **Lexical Analyzer** for UET Programming Language `(*.upl)`: \
**Input:** Source code. \
**Output:** List of tokens.

#### ________________________________

UET Programming Language is described as below:

- Statement: `if {cond} then {stmt} else {stmt};`
- Keywords: `if`, `then`, `else`
- Cond (relative operator): `>`, `<` (i.e. `a>1`, `2>1`, `a>b`)
- `{stmt}`: assign `a=b`
- **Variable name**: start with **a letter, followed by a digit**, and then followed by any number of characters either of these types (letter or digit).


### Solution
We first create class `Token` consisting of 2 values: token type and token value (lexeme). 
```py
class Token():
    def __init__(self, _type, lexeme) -> None:
        self._type = _type
        self.lexeme = lexeme
```

Our class `Scanner` is responsible for parsing a string and return a list of `Token`.
```py
class Scanner():

    def __init__(self) -> None:
        abstract

    def getTokenForm(self, content):
        abstract

    def normalize(self, content):
        abstrct

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

```
