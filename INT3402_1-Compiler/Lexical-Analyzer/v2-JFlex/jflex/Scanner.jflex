package upl;

%%
%type int
%line
%column
%char
%class Scanner
%{

	
%}
%eofval{
    System.out.println("EOF"); return 1;
%eofval}

LEFT_BRACKET = [(]
RIGHT_BRACKET = [)]

LEFT_PARENTHESIS = "{"
RIGHT_PARENTHESIS = "}"

ADD = [+]
MUL = [*]

INT_T = (int)
BOOL_T = (bool)

BEGIN = (begin)
END = (end)

CONST_BOOL = (true) | (false)
CONST_INT = [0]|[1-9][0-9]*

NOT_IDENTIFIER = [a-zA-Z]+[0-9]+[a-zA-Z]+[a-zA-Z0-9]*
IDENTIFIER = [a-zA-Z]+[0-9]*
ROP = ==|<=|>=|=|<|>
ASSIGN = [=]

DO = (do)
WHILE = (while)
IF = (if)
THEN = (then)
ELSE = (else)
PRINT = (print)
SEMICOLON = ;

ONELINE_CMT = "//".*
MULTILINE_CMT = [/][*][^*]*[*]+([^*/][^*]*[*]+)*[/]

%%

{DO} {System.out.println("(DO, " + yytext()+")"); return 0;}
{WHILE} {System.out.println("(WHILE, " + yytext()+")"); return 0;}
{IF} {System.out.println("(IF, " + yytext()+")"); return 0;}
{THEN} {System.out.println("(THEN, " + yytext()+")"); return 0;}
{ELSE} {System.out.println("(ELSE, " + yytext()+")"); return 0;}
{PRINT} {System.out.println("(PRINT, " + yytext()+")"); return 0;}
{INT_T} {System.out.println("(INT_T, " + yytext()+")"); return 0;}
{BOOL_T} {System.out.println("(BOOL_T, " + yytext()+")"); return 0;}
{BEGIN} {System.out.println("(BEGIN, " + yytext()+")"); return 0;}
{END} {System.out.println("(END, " + yytext()+")"); return 0;}
{CONST_BOOL} {System.out.println("(CONST BOOL, " + yytext()+")"); return 0;}

{ADD} {System.out.println("(ADD, " + yytext()+")"); return 0;}
{MUL} {System.out.println("(MUL, " + yytext()+")"); return 0;}
{LEFT_BRACKET} {System.out.println("(LEFT_BRACKET, " + yytext()+")"); return 0;}
{RIGHT_BRACKET} {System.out.println("(RIGHT_BRACKET, " + yytext()+")"); return 0;}
{LEFT_PARENTHESIS} {System.out.println("(LEFT_PARENTHESIS, " + yytext()+")"); return 0;}
{RIGHT_PARENTHESIS} {System.out.println("(RIGHT_PARENTHESIS, " + yytext()+")"); return 0;}
{NOT_IDENTIFIER} {System.out.println("Illegal identifier: " + yytext()+" at line " + yyline + " col " + yycolumn); return 0;}
{IDENTIFIER} {System.out.println("(IDENTIFIER, " + yytext()+")"); return 0;}
{CONST_INT} {System.out.println("(CONST INT, " + yytext()+")"); return 0;}
{ASSIGN} {System.out.println("(ASSIGN, " + yytext()+")"); return 0;}
{ROP} {System.out.println("(ROP, " + yytext()+")"); return 0;}
{SEMICOLON} {System.out.println("(SEMICOLON, " + yytext()+")"); return 0;}
{ONELINE_CMT} {;}
{MULTILINE_CMT} {;}
[/][*]    { System.out.println("Unterminated comment"); }


[ \t\r\n\f] { /* ignore white space. */ }

. { System.out.println("Illegal character: line "+yyline + " col " + yycolumn); return 0;}
