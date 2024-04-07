# Syntax Analyzer

Tham khảo: [*Compiler Midterm Review*](https://typst.app/project/p1jmwAxhIAjbgLB5KQg6zD)

## Xử lý văn phạm (Toản)
Left recursion elimination.
Left factoring.

```
S -> begin <stmtList> end

T = (){};+*=, int, bool, <Id>, <Number>, <ROP>, do, while, if, then, else, print

<stmtList>    ->  <stmt>;<stmtList> | epsilon

<stmt>  -> if <Expr> then { <stmtList> } <ifTail>
        | do { <stmtList> } while (<Expr>)
        | <Assignment>
        | <Declaration>
        | print(<Expr>)                     // should be some function or just print?

<ifTail> -> else { <stmtList> } | epsilon	// else part for IF command

<Type>          -> int | bool
<Declaration>   -> <Type> <L>
<L>             -> <L1><L2>
<L1>            -> <Id> | <Assign-stmt> 
<L2>		-> , <L> | epsilon		// Multiple variables declaration

<Assignment> -> <Id> = <Expr>               // int a = true: should be caught on next phase, not parser

<Expr>      -> <C> | <M-Expr>
<C>         -> <M-Expr> <ROP> <M-Expr>           // <ROP> is right-associative
<M-Expr>    -> <Term> <METail>
<METail>    -> + <M-Expr> | epsilon
<Y>         -> Id | Number

# right-associative
<Term>      -> <Factor> <T2>
<Factor>    -> <Y> | (<M-Expr>) 
<T2>        -> * <Term> | epsilon
```





## Cấu trúc Parser (Table-driven predictive parsing)

**Đầu vào:** Source code. Parsing Table\
**Đầu ra:** chuỗi dẫn xuất (leftmost)

Thuận góp ý và tự chỉnh sửa lại.

Parsing Table: Chapter 4. SYNTAX ANALYSIS trang 222. (giống FIRST+ nhưng đọc sách thì ok hơn)

Mỗi lúc nhận vào token tiếp theo và chọn dẫn xuất tương ứng hoặc báo lỗi.

**Ví dụ:**.
```py
from enum import IntEnum, auto
from Scanner import *

# Sau này sẽ có class Compiler để manage tương tác giữa Scanner và Parser
# Thay vì Scanner là 1 attribute của Parser -> passing arguments overhead


"""
Tại sao cần: Vẫn cần ID để phân biệt các token với nhau.
IntEnum.
"""
class SymbolType(TokenType): # NOTE: verify: derive để có sẵn các token trong đó
    # TODO: Thay đổi, vì văn phạm mới có thể có S', F' gì đó
    S = auto()
    STMT_LIST = auto()
    EXPR = auto()
    M_EXPR = auto()
    ...


class Symbol():
    """
    Trả về trong get_production(current_symbol, next_sym):
    [Symbol, Symbol, ...]
    nó khác với [SymbolType, SymbolType, ..] ở chỗ có giá trị cụ thể,
    StartToken đi kèm row, col để báo lỗi khi cần...
    """
    _type = 0  # SymbolType
    start_token = None    
    # Giả sử symbol S, 
    # dùng dẫn xuất S -> begin stmtList end  thì start_token = TokenType.BEGIN

    val = 0 # NOTE: ignore, pha sau mới dùng

    def __init__(self, name, productions = []):
        self.__name__ = name

class Grammar():
    # người dùng ko nhìn thấy
    # PRODUCTION = dict()
    # FIRST = dict()  
    # FOLLOW = dict() i.e. FOLLOW[SymbolType]
    # parse_table = None

    def get_production(current_symbol, next_sym) -> [Symbol]:
        pass
        

class Parser:
    # Output là [[Symbol],...]

    grammar = None

    s = Scanner()

    def __init__(self, grammar) -> None:
        self.grammar = grammar

    def parse(path) -> list: 
        """
        Trả về List Productions có dạng:
        [
            [BEGIN, stmtList, END],
            [Symbol, Symbol, Symbol...],
            [Symbol, Symbol],
            [..]
        ]
        
        Lý do không cần vế trái vì chúng ta parse leftmost nên 
        vế trái là non-terminal trái nhất trên cây tính đến thời điểm hiện tại.
        Mỗi lúc dẫn xuất ta chọn lại sinh các con mới cho nút hiện tại.
        """

        self.s.scan(path)


```

Parser giữ 1 stack 



| Stack   |
| --- |
| -    |
| -   |
|-  |
| **S** <--- (`stack.top()`)   | 
| $   |

**Trang 227 trong sách:**
![](https://cdn.discordapp.com/attachments/915575548959420416/1226342034806407289/image.png?ex=66246b05&is=6611f605&hm=e88bdb4f30e14e60182dc939200cf99f03020b2150d9389d2ebdee23f6accc12&)
