def reverseStr(input_string, group_size):
    result_parts = []
    string_length = len(input_string)

    for block_start in range(0, string_length, 2 * group_size):
        current_block = input_string[block_start:block_start + 2 * group_size]

        if len(current_block) < group_size:
            result_parts.append(current_block[::-1])
        else:
            reversed_part = current_block[:group_size][::-1]
            remaining_part = current_block[group_size:]
            result_parts.append(reversed_part + remaining_part)

    return "".join(result_parts)


print(reverseStr("abcdefg", 2))
print(reverseStr("abcd", 2))