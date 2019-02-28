import sys
import operator

class MouseParser:

    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.floordiv}
    def __init__(self):
        self.stack = []
        self.variables = [None] * 26
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()

    def parse(self, text):
        
        i = 0
        while i < len(text):
            char = text[i]
            if char.isdigit():
                num = int(char)
                while (i + 1) < len(text) and text[i+1].isdigit():
                    i += 1
                    num *= 10
                    num += int(text[i])
                self.push(num)
            elif char in self.ops:
                a = self.pop()
                b = self.pop()
                self.push(self.ops[char](b, a))
            elif 'a' <= char <= 'z':
                self.push(ord(char) - ord('a'))
            elif char == '.':
                self.push(self.variables[self.pop()])
            elif char == '=':
                a = self.pop()
                b = self.pop()
                self.variables[b] = a
            i += 1

if __name__ == '__main__':
    parser = MouseParser()
    parser.parse(sys.argv[1])
    print(parser.stack)