# make an interpreter
# Goal: 7  + 3 +    2 - 5  

# token type
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        # plus, minus = '+'. '-'
        self.value = value

    def __str__(self):
        return "Token({type}, {value})".format(
                type=self.type, value=self.value
                )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.current_token = None
        self.pos = 0
        self.current_char = self.text[self.pos] 

    def error(self):
        raise Exception('Invalid syntax')

    # advance will move self.pos and change self.current_char
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    # extract the integer with more than 1 digits
    def extract_int(self):
        tar_int = ''
        while(self.current_char is not None and self.current_char.isdigit()):
           tar_int += self.current_char
           self.advance()
        return int(tar_int)
    
    def get_next_token(self):
        # for current position
        while(self.current_char is not None):
            # case 1: integer
            if self.current_char.isdigit():
                this_int = self.extract_int()
                return Token(INTEGER, this_int) 

            # case 2: operator
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            # case 3: white space
            # can be made better, cuz the cost.
            if self.current_char.isspace():
                self.advance()
                continue
            
            raise Exception("parsing error: input is wrong")

        return Token(EOF, None)

    # check the current token type is expected
    def eat(self, eat_type):
        if eat_type == self.current_token.type:
            self.current_token = self.get_next_token()
        else:
            self.error()


    # check for the token type (term) and eat it
    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()
        result = self.term()
        
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token.type
            if token == PLUS:
                self.eat(PLUS)
                result += self.term()
                continue

            if token == MINUS:
                self.eat(MINUS)
                result -= self.term()
                continue
        
        return result
def main():
    while(True):
        try:
            text = input("calc3 > ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print("\n{x}\n".format(x = result))

if __name__ == "__main__":
    main()
