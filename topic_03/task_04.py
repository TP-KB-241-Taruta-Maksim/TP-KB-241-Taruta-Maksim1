def insert_sorted(sorted_list, value):
    position = find_insert_position(sorted_list, value)
    sorted_list.insert(position, value)
    return sorted_list

# Приклад
print(insert_sorted([1, 2, 4, 5], 3))
