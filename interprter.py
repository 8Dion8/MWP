#Stack accepts: int, float, string

def buildbracemap(code,op1,op2):
   temp_bracestack, bracemap = [], {}
   for position, command in enumerate(code):
       if command == op1: temp_bracestack.append(position)
       if command == op2:
           start = temp_bracestack.pop()
           bracemap[start] = position
           bracemap[position] = start
   return bracemap

def interpret(code, input_):

    if code == '':return 0, None, None

    pos = 0

    squarebracemap = buildbracemap(code, "[", "]")
    roundbracemap = buildbracemap(code, "(", ")")
    longcondbracemap = buildbracemap(code, "<", ">")
    invlongcondbracemap = buildbracemap(code, "{", "}")

    stack = []
    M = 0
    A = 0
    W = 0
    P = 0

    pushingString = False
    pushedFirstNum = False
    pushingInputNum = False

    output = ''

    while True:
        pushingInputNum = False
        op = code[pos]
        if not pushingString:
            if op in ['0','1','2','3','4','5','6','7','8','9']:
                if not pushedFirstNum:
                    stack.append(int(op))
                    pushedFirstNum = True
                else:
                    stack.append(int(str(stack.pop()) + op))
            else:
                pushedFirstNum = False

            if op == ' ':
                pushedFirstNum = True
                stack.append(0)

            elif op == '+':
                top = stack.pop()
                sec = stack.pop()
                if type(top) == str or type(sec) == str:
                    stack.append(str(sec) + str(top))
                else:
                    stack.append(top + sec)

            elif op == '-':
                top = stack.pop()
                sec = stack.pop()
                if type(top) != str and type(sec) != str:
                    stack.append(sec - top)
                else:
                    stack.extend([sec,top,0])
            
            elif op == '*':
                top = stack.pop()
                sec = stack.pop()
                if type(top) == str and type(sec) == str:
                    stack.extend([sec,top,0])
                else:
                    if type(top) == str:
                        stack.append(top*sec)
                    else:
                        stack.append(sec*top)

            elif op == '/':
                top = stack.pop()
                sec = stack.pop()
                if type(top) != str and type(sec) != str:
                    stack.append(sec / top)
                else:
                    stack.extend([sec,top,0])

            elif op == '%':
                top = stack.pop()
                sec = stack.pop()
                if type(top) != str and type(sec) != str:
                    stack.append(sec % top)
                else:
                    stack.extend([sec,top,0])

            elif op in 'MAWP':
                if code[pos-1] == '=' and code[pos-2] != '=':
                    top = stack.pop()
                    if op == 'M':
                        M = top
                    elif op == 'A':
                        A = top
                    elif op == 'W':
                        W = top
                    else:
                        P = top
                else:
                    stack.append(eval(op))

            elif op == '"':
                stack.append('')
                pushingString = True

            elif op == '`':
                stack.pop()
            
            elif op == '!':
                top = stack.pop()
                stack.append(top)
                stack.append(top)
            
            elif op == ':':
                output+=str(stack.pop())
            
            elif op == ';':
                top = stack.pop()
                if type(top) == int:
                    output+=chr(top)
                else:
                    for i in top:
                        output += str(ord(i)) + ' '

            elif op == '.':
                return 0, None, output
            
            elif op == '_':
                stack.append(len(stack))
            
            elif op == '|':
                for i in input_:
                    stack.append(ord(i))
            
            elif op == '@':
                for i in input_:
                    if i in '1234567890':
                        if pushingInputNum:
                            stack.append(stack.pop() * 10 + int(i))
                        else:
                            stack.append(int(i))
                            pushingInputNum = True
                    else:
                        pushingInputNum = False
            
            elif op == '~':
                stack = stack.reverse()
            





            elif op == ']':
                if stack[-1] != 0:
                    pos = squarebracemap[pos]

            elif op == '[':
                if stack[-1] == 0:
                    pos = squarebracemap[pos]

            elif op == ')':
                if stack[-1] == 0:
                    pos = roundbracemap[pos]

            elif op == '(':
                if stack[-1] != 0:
                    pos = roundbracemap[pos]
            
            elif op == '<':
                if stack[-1] != 0:
                    pos = longcondbracemap[pos]
            
            elif op == '{':
                if stack[-1] == 0:
                    pos = invlongcondbracemap[pos]

        else:
            if op == '"':
                pushingString = False
            else:
                stack.append(stack.pop() + op)

        pos += 1
        print(stack)
        if pos == len(code):
            return 0, None, output

if __name__ == "__main__":
    exit_code, error, output = interpret('@','123lol43')