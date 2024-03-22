
### Our group: 

- 21020055 Trần Thùy Dung 
- 21020037 Nguyễn Đức Thuận 
- 21020455 Lê Quốc Toản

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

## 19/03/2024: 5h20-7h45 Toan & Dung working on grammar and scanner
TODO:  Dung

- regex for comments: van de do split() cac words
- parser
- color printer

## 21/03/2024

**Steps for making Parser.**

- Eliminate left recursion
- Loai bo de quy gian tiep
- FIRST & FOLLOW

## 22/03/2024: 10PM
Grammar
