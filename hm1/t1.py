def is_prime(n):
    count_del = 0
    for i in range(1, n+1):
        if n % i == 0:
            count_del += 1
    if count_del == 2:
        return True
    else:
        return False


# print(is_prime(13))

N = int(input())
s = 0
for i in range(2, N+1):
    if is_prime(i):
        s += i
print(s)

#2 3 4 5 6 7 8 9 10 -> 17