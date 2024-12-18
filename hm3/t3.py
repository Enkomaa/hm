def capitalize(letter):
    first_bukva = letter[0]
    idx_first_bukva = ord(first_bukva)
    idx_big_first_bukva = idx_first_bukva - 32
    return chr(idx_big_first_bukva)+letter[1:]

source = input().split()
res = []
for letter in source:
    res.append(capitalize(letter))
print(' '.join(res))
