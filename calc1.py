# Token type
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'
MINUS = 'MINUS'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
                type=self.type, value=repr(self.value)
                )

    # This would automatically becomes the way to print this 
    # object. Otherwise, only <object token> of some sort will
    # be printed.
    def __repr__(self): return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text 
        # this pos index indicates the position to be parsed next.
        self.pos = 0
        self.current_token = None
    
    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        while(self.text[self.pos] == ' '):
            self.pos += 1
            if self.pos > len(self.text) - 1:
               return Token(EOF, None)

        current_char = self.text[self.pos]
        
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token
        
        return self.error()
    
    def eat(self, token_type):
        # This function is to check the format of the operation
        # is as expected : INTEGER -> PLUS -> INTEGER
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        # left operhand
        left = ''
        flag = self.current_token.type
        while(flag == INTEGER):
            left += str(self.current_token.value)
            self.eat(INTEGER)
            flag = self.current_token.type        
            
        # operator
        # opflag:
        #   0 : +
        #   1 : -
        opflag = 0
        op = self.current_token 
        if self.current_token.type == PLUS:
            self.eat(PLUS)
        elif self.current_token.type == MINUS:
            self.eat(MINUS)
            opflag = 1
        else:
            raise Exception("Operator parsing error! ")

        # right operhand
        right = ''
        flag = self.current_token.type
        while(flag == INTEGER):
            right += str(self.current_token.value)
            self.eat(INTEGER)
            flag = self.current_token.type 
        

        if opflag:
            result = int(left) - int(right)
        else: 
            result =  int(left) + int(right)
        return result

def main():
    while True: 
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue 
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
