#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = []
    sum_uniq = 0
    for num in my_list:
        if num not in uniq_int:
            uniq_int.append(num)
            sum_uniq += num
    return sum_uniq
