#Stack accepts: int, float, string

def buildbracemap(code,char1,char2):
   temp_bracestack, bracemap = [], {}
   for position, command in enumerate(code):
       if command == char1: temp_bracestack.append(position)
       if command == char2:
           start = temp_bracestack.pop()
           bracemap[start] = position
           bracemap[position] = start
   return bracemap

def interpret(code):

    if code == '':return 1

    pos = 0

    stack = []
    M = 0
    A = 0
    W = 0
    P = 0

    pushingString = False
    pushedFirstNum = False


    while True:
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
                    stack.append(str(top) + str(top))
                else:
                    stack.append(top + sec)
            elif op in 'MAWP':
                if code[pos-1] == '=':
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
        else:
            if op == '"':
                pushingString = False
            else:
                stack.append(stack.pop() + op)

        pos += 1
        print(stack)
        if pos == len(code):
            return 0
interpret('63=MMM+=MM')