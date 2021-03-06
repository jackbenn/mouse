import sys
import operator
import time

class StackFrame:
    def __init__(self, type, pos, base):
        self.type = type
        self.base = base
        self.pos = pos

class MouseParser:
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.floordiv,
           '\\': operator.mod,
           '=': operator.eq,
           '<': operator.lt,
           '>': operator.gt
           '=': operator.eq}
    def __init__(self):
        self.stack = []
        self.loop_stack = []
    
        self.variable_base = 0
        self.variables = [None] * 26
    
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()
    
    def get_variable(self, i):
        return self.variables[i + self.variable_base * 26]

    def get_variable(self, i, value):
        self.variables[i + self.variable_base * 26] = value
    
    def find_next(self, text, i, char):
        """Return next instance of char in the text starting at i"""
        return text
    
    def push_frame(self, ):
        

    def pop_frame(self):

        return 

    def parse(self, text):
        """parse and execute a mouse program"""
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
                self.push(int(self.ops[char](b, a)))
            elif char == '!':
                print(self.pop())
            elif char == '"':
                while True:
                    i += 1
                    if text[i] == '"':
                        break
                    if text[i] == '!':
                        print()
                    else:
                        print(text[i], end='')
            elif char == '?':
                self.push(int(input()))
            elif 'a' <= char <= 'z':
                self.push(ord(char) - ord('a'))
            elif char == '.':
                self.push(self.variables[self.pop()])
            elif char == ':':
                a = self.pop()
                b = self.pop()
                self.variables[a] = b
            elif char == '(':
                self.loop_stack.append(i)
            elif char == ')':
                i = self.loop_stack.pop() - 1
            elif char == '^':
                if self.pop() == 0:
                    i = text.index(')', i)
            elif char == '[':
                if self.pop() == 0:
                    i = text.index(']', i)
            elif char == ']':
                pass
            elif char in [' ', '\n']:
                pass
            elif char == '$':
                return True
            else:
                raise IndexError(f"Invalid character {char}")
            i += 1
            time.sleep(0.01)
        return False


if __name__ == '__main__':
    parser = MouseParser()
    text = sys.stdin.read()
    parser.parse(text)
    print(parser.stack)
    print(parser.variables)
