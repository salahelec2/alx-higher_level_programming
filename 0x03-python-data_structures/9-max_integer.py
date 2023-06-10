def max_integer(my_list):
    if len(my_list) == 0:
        return None  # Return None for an empty list
    old_val = my_list[0]
    for i in my_list:
        if i > old_val:
            old_val = i
    return old_val
