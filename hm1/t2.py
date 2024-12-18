s = input()
s = s.replace(' ', '')
s = s.lower()
n = len(s)
ans = True
for i in range(n // 2):
    # print(s[i], s[n - 1 - i])
    if s[i] != s[n - 1 - i]:
        ans = False
        break

print(ans)