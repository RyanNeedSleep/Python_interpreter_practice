# my expression interpreter
# Goal: 1 + 2 + 5 - 4 - 2

# Token type: INTEGER, OPERATOR, EOF
INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self. type = type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
                type = self.type,
                value = self.value
                )
    
    def __repr__(self):
        return self.__str__()

    def __get_val__(self):
        return self.value

    def __get_type__(self):
        return self.type

class Interpreter(object):
    def __init__(self, text):

        self.text = text 
        self.pos = 0 
        self.current_char = self.text[self.pos]
        self.current_token = None
    
    # lexcial analysis: tokenizer
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue
            
            if self.current_char.isdigit():
                val = self.get_int()
                return Token(INTEGER, val)

            if self.current_char == '+':
                self.advance()
                return Token(OPERATOR, '+')

            if self.current_char == '-':
                self.advance()
                return Token(OPERATOR, '-')
            
            raise Exception('Error in tokenizer: invalid input character')
        
        return Token(EOF, None)
    
    # update self.crrent_char
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def get_int(self):
        tar_int = ''

        while self.current_char.isdigit():
            tar_int += self.current_char
            self.advance()

            if self.current_char == None:
                break    

        return int(tar_int)

    # update current_token
    def syntax_eat(self, type):
        if type == self.current_token.__get_type__():
            token_val = self.current_token.__get_val__()
            self.current_token = self.get_next_token()
            return token_val
        else:
            raise Exception('Invalid syntax')
    
    # term
    def term(self):
        return self.syntax_eat(INTEGER)

    # Syntax analysis
    def expr(self):
        self.current_token = self.get_next_token() 
        result = self.term() 

        while(self.current_token.__get_type__() == OPERATOR):
            token = self.syntax_eat(OPERATOR)

            if token == '+':
                result += self.term()
            elif token == '-':
                result -= self.term()
        
        return result

def main():
    while True:
        try:
            text = input('my_calc > ')
        except KeyboardInterrupt:
            print("\n\nEnd of the program\n")
            break
        
        if not text: 
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()

        print("\n{}\n".format(result))

if __name__ == '__main__':
    main()

                
        

        
        




