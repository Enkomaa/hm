s = input('Введите скобки:')
def is_norm_skobki(s):
    stack = []
    d = {
    '(': ')',
    '{': '}',
    '[': ']'}
    for elem in s:
        if elem in d.keys(): # если elem открыв. скобка?
            stack.append(elem)
        else: # если elem закрыв. скобка?
            if len(stack) == 0:
                return False
            t = stack.pop()
            if d[t] != elem:
                return False
    return True
print("Скобки закрыты верно:", is_norm_skobki(s))