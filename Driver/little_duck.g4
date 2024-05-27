grammar little_duck; 

//Tokens 
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
PUNTOYCOMA : ';' ;
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


//reg ex 
   
    ID: [a-zA-Z][a-zA-Z_0-9]*;
    CTE_FLOAT: [0-9]+ '.' [0-9]+;
    CTE_INT: [0-9]+;
    CTE_STRING: '"' .*? '"'; 
    WS : [ \t\n\r]+ -> skip ;
//



//Programa 
    start_: PROGRAM ID PUNTOYCOMA (vars)? (funcs)* MAIN body END;
//

//vars 
    vars: VAR (var0)+;

    var0: var1 ':' type PUNTOYCOMA var2;

    var1: ID | var1 COMA ID;

    var2:  (var1)? ;
//

//type 
    type: FLOAT | INT;
//

//Body 
    body: LLAVEI (statement)* LLAVED; 
//

//statement 
    statement: assign | condition | cycle | f_call | print;
//

//assign 
    assign: ID IGUAL expression PUNTOYCOMA;
//

//print 

    print: PRINTF PARI print0 PARD PUNTOYCOMA ;

    print0: expression print1 |  CTE_STRING print1;

    print1:  (COMA print0)?;  

//

//cycle 
    cycle: DO body WHILE PARI expression PARD PUNTOYCOMA;
//

//condition 
    condition: IF PARI expression PARD body condition0;

    condition0: (ELSE body )? PUNTOYCOMA; 
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
    factor: PARI expression PARD
        | factor0 factor1;

    factor0: (MAS | MENOS )?;

    factor1: ID | cte;
//

//Funcs 
    funcs: VOID ID PARI funcs0 PARD '[' funcs3 body ']' PUNTOYCOMA;

    funcs0: ( funcs1)?;

    funcs1: ID ':' type funcs2;

    funcs2: (COMA funcs1)?;

    funcs3: (vars)?;
//

//f_call 
    f_call: ID PARI f_call0 PARD PUNTOYCOMA;

    f_call0:  (f_call1)?;

    f_call1: expression f_call2;

    f_call2: (COMA f_call1)?;
//





