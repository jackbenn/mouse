import sys

class MouseParser:
    def __init__(self):
        self.stack = []
    
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
                self.stack.append(num)

            i += 1

if __name__ == '__main__':
    parser = MouseParser()
    parser.parse(sys.argv[1])
    print(parser.stack)