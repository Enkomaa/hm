def merge_dicts(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:
            if isinstance(merged[key], list):
                merged[key].append(value)
            else:
                merged[key] = [merged[key], value]
        else:
            merged[key] = value

    return merged

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)