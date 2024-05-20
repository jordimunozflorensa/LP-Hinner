grammar hm;

root: typing* expr? typing* EOF;

typing: (OPER | NUM) PP TYPE (ARROW TYPE)*;

expr: LPAR expr RPAR                        # paren 
    | expr expr                             # app
    | <assoc=right> CBAR ID ARROW expr      # lambda
    | OPER                                  # oper
    | ID                                    # idexpr
    | NUM                                   # numexpr
    ;

OPER      : ('(*)' | '(/)' | '(+)' | '(-)') ;
LPAR      : '(' ;
RPAR      : ')' ;
ARROW     : '->' ;
CBAR      : '\\' ;
PP        : '::' ;
ID        : [a-z] [a-zA-Z]* ;
TYPE      : [A-Z] [a-zA-Z]* ;
NUM       : [0-9]+ ;
WS        : [ \t\n\r]+ -> skip ;
