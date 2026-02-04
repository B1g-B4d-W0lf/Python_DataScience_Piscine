import numpy as np
# import sys


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise AssertionError("Wrong type of arguments")
        if len(height) != len(weight):
            raise AssertionError("Lists are not the same lenght")
        if (not all(isinstance(i, (int, float)) for i in height) or
       not all(isinstance(i, (int, float)) for i in weight)):
            raise AssertionError("Not all arguments are integer or float")
    except AssertionError as e:
        print(e)
        return []

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    
    bmi_cal = lambda h, w: w / (h * h)
    
    res_func = np.frompyfunc(bmi_cal, 2, 1)

    result = res_func(height_arr, weight_arr)

    return list(result)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not isinstance(bmi, list) or not isinstance(limit, int):
            raise AssertionError("Wrong types of arguments")
        if not all(isinstance(i, (int, float)) for i in bmi):
            raise AssertionError("Not all arguments are integer or float")
    except AssertionError as e:
        print(e)
        return []

    limit_cal = lambda b, l: b > l
    bmi_arr = np.array(bmi)
    result = np.frompyfunc(limit_cal, 2, 1)

    return list(result(bmi_arr, limit))
