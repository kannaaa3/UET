# Simple Lexical Analyzer Implementation

## Table of Contents
1. [📑Context-free Grammar](#grammar)
2. [⚙️ Implementing Lexical Analyzer](#implementing)
3. [🍒 Run](#run)
4. [👤 Our team](#team)


## 📑 \ Context-free Grammar <a name="grammar"></a>

```
S -> begin <stmtList> end

T = (){};+*=, int, bool, <Id>, <Number>, <ROP>, do, while, if, then, else, print

<stmtList>    ->  <stmt>;<stmtList> | epsilon

<stmt>  -> if <Expr> then { <stmtList> }
        | if <Expr> then { <stmtList> } else { <stmtList> } 
        | do { <stmtList> } while (<Expr>)
        | <Assignment>
        | <Declaration>
        | print(<Expr>)                     // should be some function or just print?


<Type>          -> int | bool
<Declaration>   -> <Type> <L>
<L>             -> <L1>,  <L> | <L1>        // Multiple variables declaration
<L1>            -> <Id> | <Assign-stmt> 

<Assignment> -> <Id> = <Expr>               // int a = true: should be caught on next phase, not parser

```


```
<Expr>      -> <C> | <M-Expr>
<C>         -> <M-Expr> <ROP> <M-Expr>           // <ROP> is right-associative
<M-Expr>    -> <Term> + <M-Expr> | <Term>
<Y>         -> Id | Number

# right-associative
<Term>      ->  <Factor> * <Term> |   <Factor> 
<Factor>    -> <Y> | (<M-Expr>) 
```

## \ ⚙️  Implementing  <a name="implementing"></a>

### a. Coding Scanner

```py
class TokenType(IntEnum):
    DO = auto()
    WHILE = auto()
    IF = auto()
    ...

class Token(token_t: TokenType, lexeme: str, col: int, row: int)

class Scanner():
    # defined regex here
    # regex[TokenType.DO] = r"do\b"
    # ...
    def scan(self, path: str) -> None:
        # Parse a file into scanner
        pass

    def nextToken(self) -> Token:
        # return the next token
        pass
```

#### Output
```py
# pseudo code for testing
def main():
    scanner.scan("./inp")
    while token = scanner.nextToken():
        if token.type is EOF: break
        if token.type is UNKNOWN: alert(), exit()
        print(token)
```

![](https://cdn.discordapp.com/attachments/915575548959420416/1223127770276560936/example.png?ex=6618b981&is=66064481&hm=0b8d5607051fe5f6b2f38f871fcae49396cdc861ea5d3c8680e604c0a0b7abb4&)

### b. Using `JFlex`
Defining regex for tokens and the program's behaviour when encountering these tokens:
```java
CONST_BOOL = (true) | (false)
CONST_INT = [0]|[1-9][0-9]*
WHILE = (while)
IDENTIFIER = [a-zA-Z]+[0-9]*
...
{CONST_BOOL} {System.out.println("(CONST BOOL, " + yytext()+")"); return 0;}
{CONST_INT} {System.out.println("(CONST INT, " + yytext()+")"); return 0;}
{DO} {System.out.println("(DO, " + yytext()+")"); return 0;}
{WHILE} {System.out.println("(WHILE, " + yytext()+")"); return 0;}
{ONELINE_CMT} {;}
{MULTILINE_CMT} {;}
```

## 🍒 Run <a name="run"></a>

### v1-Coding
```sh
~/Compiler/Lexical-Analyzer/v1-Code  ··································································
❯ ./Scanner.py file_path
```


### v2-JFlex
Build 
```sh
~/Compiler/Lexical-Analyzer/v2-JFlex  ··································································
❯  ant
```
Run:
```sh
~/Compiler/Lexical-Analyzer/v2-JFlex ··································································
❯  java -jar dist/Compiler.jar < {path-to-input-file}
```

## 👤 Our team <a name="team"></a>

- 21020055 Tran Thuy-Dung
- 21020037 Nguyen Duc-Thuan
- 21020455 Le Quoc-Toan
