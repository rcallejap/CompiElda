grammar little_duck; 

//reg ex 
   
    ID: [a-zA-Z][a-zA-Z_0-9]*;
    CTE_FLOAT: [0-9]+ '.' [0-9]+;
    CTE_INT: [0-9]+;
    CTE_STRING: '"' .*? '"'; 
    WS : [ \t\n\r]+ -> skip ;
//



//Programa 
    start_: 'program' ID ';' (vars)? (funcs)* 'main' body 'end';
//

//vars 
    vars: 'var' (var0)+;

    var0: var1 ':' type ';' var2;

    var1: ID | var1 ',' ID;

    var2:  (var1)? ;
//

//type 
    type: 'float' | 'int';
//

//Body 
    body: '{' (statement)* '}'; 
//

//statement 
    statement: assign | condition | cycle | f_call | print;
//

//assign 
    assign: ID IGUAL expression ';';
//

//print 

print: 'printf' '(' print0 ')' ';' ;

print0: expression print1 |  CTE_STRING print1;

print1:  (',' print0)?;  

//

//cycle 
    cycle: 'do' body 'while' '(' expression ')' ';';
//

//condition 
    condition: 'if' '(' expression ')' body condition0;

    condition0: ('else' body ';')?; 
//

//expression 
    expression: exp expression0;

    expression0:  (expression1 exp)?;

    expression1: MAYOR | MENOR | DIF;
//

//exp 
    exp: termino exp0;

    exp0:  (exp1 exp)?;

    exp1: MENOS | MAS;
//


//cte 
    cte: CTE_FLOAT | CTE_INT;
//


//Termino 
    termino: factor termino0;

    termino0: ( termino1 termino)?;

    termino1: POR | DIV;
//

//factor 
    factor: '(' expression ')'
        | factor0 factor1;

    factor0: (MAS | MENOS )?;

    factor1: ID | cte;
//

//Funcs 
    funcs: 'void' ID '(' funcs0 ')' '[' funcs3 body ']' ';';

    funcs0: ( funcs1)?;

    funcs1: ID ':' type funcs2;

    funcs2: (',' funcs1)?;

    funcs3: (vars)?;
//

//f_call 
    f_call: ID '(' f_call0 ')' ';';

    f_call0:  (f_call1)?;

    f_call1: expression f_call2;

    f_call2: (',' f_call1)?;
//




MAS: '+';
MENOS: '-';
POR : '*';
DIV : '/';
MENOR : '<';
MAYOR : '>';
DIF : '!=';
IGUAL : '=';
PARI : '(';
PARD : ')';
LLAVEI : '{';
LLAVED : '}';
COMA : ',';
PUNTOYCOMA : ';';
IF : 'if';
ELSE : 'else';
DO : 'do';
WHILE : 'while';
VAR : 'var';
FLOAT : 'float';
INT : 'int';
PRINTF : 'printf';
PROGRAM : 'program';
END : 'end';
VOID : 'void';
MAIN : 'main';

