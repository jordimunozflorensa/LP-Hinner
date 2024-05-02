grammar exprs;

root: expr+;

expr: ID
    | NUM
    | '(' expr ')'
    |
    ;

ID  : ('a'..'z')+;
NUM : [0-9]+ ;
