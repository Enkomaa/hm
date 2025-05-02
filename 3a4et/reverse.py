def reverseStr(s, k):
    result = []
    string_length = len(s)

    for start_index in range(0, string_length, 2 * k):
        block = s[start_index:start_index + 2 * k]

        if len(block) < k:
            result.append(block[::-1])
        else:
            result.append(block[:k][::-1] + block[k:])

    return "".join(result)

print(reverseStr("abcdefg", 2))
print(reverseStr("abcd", 2))