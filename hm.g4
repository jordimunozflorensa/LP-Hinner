grammar hm;

root: expr+;

expr: ID
    | NUM
    | LPAR expr RPAR
    | 
    ;

PLUS      : '+' ;
MINUS     : '-' ;
MUL       : '*' ;
DIV       : '/' ;
LPAR      : '(' ;
RPAR      : ')' ;
ARROW     : '->' ;
CBAR      : '\\'  ;
ID        : ('a'..'z')+ ;
NUM       : [0-9]+ ;
WS        : [ \t\n\r]+ -> skip ;