def get_row(rowIndex):
    row = [1]

    for current_row_index in range(rowIndex):
        new_row = [1]
        for element_index in range(1, len(row)):
            new_row.append(row[element_index - 1] + row[element_index])
        new_row.append(1)
        row = new_row

    return row

print(get_row(6))
