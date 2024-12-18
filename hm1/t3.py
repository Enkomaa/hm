s = input()
stack = []
for i in s.split(' '):
    if i.isdigit():
        stack.append(int(i))
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b // a)
print(stack[0])