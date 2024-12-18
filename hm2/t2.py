from collections import deque

first_list = deque([1, 3, 5, 7])
second_list = deque([2, 4, 6, 8])
third_list = deque()

while first_list or second_list:
    if first_list:
        third_list.append(first_list.popleft())
    if second_list:
        third_list.append(second_list.popleft())

print(sorted(third_list))