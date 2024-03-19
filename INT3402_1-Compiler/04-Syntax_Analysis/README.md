<h1 align="center"> 🔹 Lexical Analyzer 🔹</h1>

### Our group: 

- 21020055 Trần Thùy Dung 
- 21020037 Nguyễn Đức Thuận 
- 21020455 Lê Quốc Toản

```
S -> begin <Statements> end

T = ;+*

<Statements>    -> <Statement> | <Statement>;<Statements>
                -> epsilon

<Statement> -> if <Expr> then <Expr>
            | if <Expr> then <Statement> else <Statement>
            | print <Expr>
            | do <Statements> while <Expr>
            | Assign????? //TODO
            | print(<Expr>)



<Assign-Statement> -> <Identifier> <ASSIGN> <Expr>


<Y> -> Id | Number
<Expr>  -> <Expr> <ROP> <Expr>
        -> <Expr> + <Term>
        -> <Term>

<Term>  ->  <Factor> * Term
        |   <Factor>

<Factor> -> <Y>
        | (<Expr>)


<COMMENT>



```

## 19/03/2024: 5h20-7h45 Toan & Dung working on grammar and scanner
TODO:   

- regex for comments: van de do split() cac words
- parser
- color printer


