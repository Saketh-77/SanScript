from datetime import datetime
from datetime import date
import ply.yacc as yacc
from main import tokens

satyastya = {
    True : 'satya',
    False : 'asatya'
}
vAra = {
    'Monday':'somavAra',
    'Tuesday':'maGgalavAra',
    'Wednesday':'budhavAra',
    'Thursday':'guruvAra',
    'Friday':'zukravAra',
    'Saturday':'zanivAra',
    'Sunday':'ravivAra'
}

def p_start_grammar(p):
    '''s : expression
            | forloop '''
    p[0] = p[1]

# Variable Declarations & Assignments
# Conditional Statments ( Excluding IF-ELSE )
def p_expression_conditionals(p):
    '''expression : kim expression pratiprati term
                    | kim expression na pratiprati term
                    | kim expression bhUyas term
                    | kim expression na bhUyas term
                    | kim expression yavIyas term
                    | kim expression na yavIyas term'''

    if p[3] == 'pratiprati':
        p[0] = satyastya[p[2] == p[4]]
    elif p[3] == 'na' and p[4] == 'pratiprati':
        p[0] = satyastya[p[2] != p[5]]    
    elif p[3] == 'bhUyas':
        p[0] = satyastya[p[2] > p[4]]
    elif p[3] == 'na' and p[4] == 'bhUyas':
        p[0] = satyastya[p[2] <= p[5]]      
    elif p[3] == 'yavIyas':
        p[0] = satyastya[p[2] < p[4]]
    elif p[3] == 'na' and p[4] == 'yavIyas':
        p[0] = satyastya[p[2] >= p[5]] 

# IF - ELSE Constructs
# Looping Constructs
def p_forloop(p):
    'forloop : forkey factor expression'
    for i in range(int(p[2])):
        print(p[3])

def p_forkey(p):
    'forkey : yAvat_parikrama' 
    pass

# Arithmatic Expressions
def p_expression_plus(p):
    'expression : expression yojanam term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression vyavakalanam term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term bahulIkaraNa factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    '''term : term pUrNasaGkhya vibhaajaka factor
            | term carabindusaGketaka vibhaajaka factor'''
            
    if p[2] == 'pUrNasaGkhya' and p[3] == 'vibhaajaka':
        p[0] = int(p[1]//p[4])
    elif p[2] == 'carabindusaGketaka' and p[3] == 'vibhaajaka':
        p[0] = p[1]/p[4]    

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : sankhyaa'
    p[0] = p[1]

def p_factor_expr(p):
    '''factor : vaamahastah_laghukosthakam expression dakSiNa_laghukosthakam'''
    p[0] = p[2]

# Date & Time
def p_date_time(p):
    '''expression : adya kaH samayaH'''
    p[0] = datetime.now().strftime("%H:%M")

def p_date_day(p):
    '''expression : adya kaH vAsaraH'''
    p[0] = vAra[datetime.now().strftime("%A")]
    
# Printing Statements
def p_print_statement(p):
    '''expression : pradarzaka vaamahastah_laghukosthakam print_input dakSiNa_laghukosthakam'''
    print('aham pradarzana : ',p[3])

def p_print_input(p):
    '''print_input : naaman
                    | expression'''
    p[0] = p[1]  
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

if __name__=="__main__":
    # Build the parser
    parser = yacc.yacc()

    while True:
        try:
            s = input('SanScript > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)