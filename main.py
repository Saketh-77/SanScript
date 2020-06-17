# SanScript - Sanskrit as a programming language
import ply.lex as lex

# Input data
data = '''
 3 + 4 * 10
   + -20 *2
 '''

# Reserved words lookup
reserved = {
    'if':'yadi',
    'else':'aaho',
    'while':'parikrama'
}
# Tokens
tokens = [
    'sankhyaa',
    'yojanam',
    'vyavakalanam',
    'bahulIkaraNa',
    'vibhaajaka',
    'vaamahastah_laghukosthakam',
    'dakSiNa_laghukosthakam',
    'naaman',
    'pratiprati',
    'bhUyas',
    'yavIyas',
    'na',
    'kim',
    'pradarzaka',
    'pUrNasaGkhya',
    'carabindusaGketaka',
    'kaH',
    'samayaH',
    'adya',
    'vAsaraH',
    'yAvat_parikrama'] + list(reserved.values())

# Token Identifiers
t_vaamahastah_laghukosthakam = r'\('
t_dakSiNa_laghukosthakam = r'\)'

# Ignoring Tokens
t_ignore = r' \t'

# Token Rules
def t_yAvat_parikrama(t):
    r'yAvat_parikrama'
    t.type = 'yAvat_parikrama'
    return t

def t_pradarzaka(t):
    r'pradarzaka'
    t.type = 'pradarzaka'
    return t

def t_kim(t):
    r'kim'
    t.type = 'kim'
    return t
    
def t_pratiprati(t):
    r'pratiprati'
    t.type = 'pratiprati'
    return t

def t_bhUyas(t):
    r'bhUyas'
    t.type = 'bhUyas'
    return t

def t_yavIyas(t):
    r'yavIyas'
    t.type = 'yavIyas'
    return t

def t_yojanam(t):
    r'yojanam'
    t.type = 'yojanam'
    return t

def t_vyavakalanam(t):
    r'vyavakalanam'
    t.type = 'vyavakalanam'
    return t

def t_bahulIkaraNa(t):
    r'bahulIkaraNa'
    t.type = 'bahulIkaraNa'
    return t

def t_vibhaajaka(t):
    r'vibhaajaka'
    t.type = 'vibhaajaka'
    return t

def t_pUrNasaGkhya(t):
    r'pUrNasaGkhya'
    t.type = 'pUrNasaGkhya'
    return t

def t_carabindusaGketaka(t):
    r'carabindusaGketaka'
    t.type = 'carabindusaGketaka'
    return t    

def t_na(t):
    r'na'
    t.type = 'na'
    return t

def t_kaH(t):
    r'kaH'
    t.type = 'kaH'
    return t

def t_adya(t):
    r'adya'
    t.type = 'adya'
    return t

def t_samayaH(t):
    r'samayaH'
    t.type = 'samayaH'
    return t

def t_vAsaraH(t):
    r'vAsaraH'
    t.type = 'vAsaraH'
    return t
    
def t_naaman(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'naaman')
    return t

def t_sankhyaa(t): # Argument to a function is an instance of a LexToken
    r'[0-9]([.][0-9]+){0,1}'
    t.value = float(t.value) # t.value is the actual lexeme, the text matched with the input
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_moghIkaroti(t):
    r'\#.*'
    pass    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
if __name__=="__main__":
    # Feed the data to lexer
    lexer.input(input('Enter keyword : '))

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)