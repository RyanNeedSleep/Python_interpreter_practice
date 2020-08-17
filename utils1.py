class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
                type=self.type,
                value=self.value
                )

    def __repr__(self):
        return __str__()

    def get_val(self):
        return self.value

    def get_type(self):
        return self.type

class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_token = None

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def get_int(self):
        tar_int = ''
        
        while self.current_char.isdigit(): 
            tar_int += self_char
            self.advance()
            if self.current_char == None:
                break
        
        return int(tar_int)

    def get_next_token(self):
        while True:
            if self.current_char.isspace():
                self.advance()
                continue
            
            if self.current_char.isdigit():
                val = self.get_int()
                return Token(INTEGER, val)

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == None:
                return Toke(EOF, None)
            
            raise Exception('Error: invalid input character')

