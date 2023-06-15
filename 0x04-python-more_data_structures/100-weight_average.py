#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    result = float(0)
    devided_by = float(0)
    for item in my_list:
        result += (item[0] * item[1])
        devided_by += item[1]
    return (result / devided_by)
