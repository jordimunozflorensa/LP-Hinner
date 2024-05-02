grammar hm;

root: stmts;

stmts: stmt+;

stmt: expr
    | apl
    | lam
    ;

lam: CBAR ID ARROW expr expr expr
    | LPAR lam RPAR
    | LPAR oper RPAR
    ;

apl: apl expr
    | lam
    ;

expr: ID   
    | NUM
    | LPAR expr RPAR
    ;

oper: PLUS
    | MINUS
    | MUL
    | DIV
    ;

PLUS      : '+' ;
MINUS     : '-' ;
MUL       : '*' ;
DIV       : '/' ;
LPAR      : '(' ;
RPAR      : ')' ;
ARROW     : '->' ;
CBAR      : '\\' ;
ID        : ('a'..'z')+ ;
NUM       : [0-9]+ ;
WS        : [ \t\n\r]+ -> skip ;